from dataclasses import dataclass, replace
from hashlib import sha256

ARTIFACT = b'agent-release:v1'
OTHER = b'agent-release:v2'
DIGEST = sha256(ARTIFACT).hexdigest()
OTHER_DIGEST = sha256(OTHER).hexdigest()
IDENTITY = 'https://github.com/example/agent/.github/workflows/build.yml@refs/heads/main'
ISSUER = 'https://token.actions.githubusercontent.com'
BUILDER = 'https://github.com/example/agent/actions/build'
SOURCE = 'example/agent@commit-abc'
PREDICATE = 'https://slsa.dev/provenance/v1'

@dataclass(frozen=True)
class Observation:
    subject: str = DIGEST
    signature_verified: bool = True
    identity: str = IDENTITY
    issuer: str = ISSUER
    trusted_root: bool = True
    builder: str = BUILDER
    source: str = SOURCE
    predicate: str = PREDICATE
    deployment_digest: str = DIGEST
    policy_allow: bool = True
    runtime_id: str | None = 'run-1'
    semantic_accepted: bool = True

def gates(x):
    metadata_present = bool(x.subject and x.builder)
    provenance_accepted = all((
        metadata_present, x.subject == DIGEST, x.signature_verified,
        x.identity == IDENTITY, x.issuer == ISSUER, x.trusted_root,
        x.builder == BUILDER, x.source == SOURCE, x.predicate == PREDICATE,
    ))
    deployment_authorized = all((provenance_accepted,
                                 x.deployment_digest == DIGEST, x.policy_allow))
    runtime_accepted = all((deployment_authorized,
                            bool(x.runtime_id), x.semantic_accepted))
    return (metadata_present, provenance_accepted,
            deployment_authorized, runtime_accepted)

base = Observation()
cases = {
    'baseline': (base, (True, True, True, True)),
    'subject_wrong': (replace(base, subject=OTHER_DIGEST), (True, False, False, False)),
    'signature_unverified': (replace(base, signature_verified=False), (True, False, False, False)),
    'identity_wrong': (replace(base, identity='other-workflow'), (True, False, False, False)),
    'issuer_wrong': (replace(base, issuer='other-issuer'), (True, False, False, False)),
    'root_untrusted': (replace(base, trusted_root=False), (True, False, False, False)),
    'builder_wrong': (replace(base, builder='other-builder'), (True, False, False, False)),
    'source_wrong': (replace(base, source='example/agent@commit-def'), (True, False, False, False)),
    'predicate_wrong': (replace(base, predicate='https://example.test/other'), (True, False, False, False)),
    'deployment_wrong': (replace(base, deployment_digest=OTHER_DIGEST), (True, True, False, False)),
    'admission_denied': (replace(base, policy_allow=False), (True, True, False, False)),
    'runtime_missing': (replace(base, runtime_id=None), (True, True, True, False)),
    'semantic_rejected': (replace(base, semantic_accepted=False), (True, True, True, False)),
}
assertions = 0
for name, (item, expected) in cases.items():
    actual = gates(item)
    for idx, (a, e) in enumerate(zip(actual, expected)):
        assert a == e, (name, idx, a, e)
        assertions += 1
counts = tuple(sum(gates(x)[i] for x, _ in cases.values()) for i in range(4))
for actual, expected in zip(counts, (13, 5, 3, 1)):
    assert actual == expected, (actual, expected)
    assertions += 1
assert DIGEST != OTHER_DIGEST
assertions += 1
print(f'cases={len(cases)} assertions={assertions} metadata={counts[0]} provenance={counts[1]} deployment={counts[2]} runtime={counts[3]} negative_metadata_shortcuts={counts[0]-counts[3]}')
