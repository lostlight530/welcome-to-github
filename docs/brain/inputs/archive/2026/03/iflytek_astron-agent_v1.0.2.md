# ℹ️ Intel: iflytek/astron-agent v1.0.2
> Source: GitHub Releases
> Date: 2026-03-07T13:10:26.807530
> **Analysis**: ⚠️ Breaking-Change

## 📝 Summary
v1.0.2

## 🔍 Changelog (Extract)
## What's Changed

### ✨ New Features
- remove auth check from import/export endpoints
- enhance RPA setup with new services and configurations (#921)
- add auto database creation and improve migration lock mechanism

### 🐛 Fixes
- restore mypy ignore-missing-imports flag
- code quality and aiohtpp client bug fix

### 🔧 Improvements
- introduce DatabaseConfig for DB config
- optimize packet guiding exceptions
- exclude enterprise watchdog feature from mypy checks

## What's Changed
* fix(aitools): code quality and aiohtpp client bug fix by @zijian2 in https://github.com/iflytek/astron-agent/pull/911
* chore: exclude enterprise watchdog feature from mypy checks by @hygao1024 in https://github.com/iflytek/astron-agent/pull/912
* 添加插件导入导出功能 by @Xxbys752521 in https://github.com/iflytek/astron-agent/pull/913
* feat: add auto database creation and improve migration lock mechanism by @cumthxy in https://github.com/iflytek/astron-agent/pull/910
* fix(ci): restore mypy ignore-missing-imports flag by @cumthxy in https://github.com/iflytek/astron-agent/pull/924
* feat(docker): enhance RPA setup with new services and configurations by @doctorbruce in https://github.com/iflytek/astron-agent/pull/921
* feat(toolkit): remove auth check from import/export endpoints by @Xxbys752521 in https://github.com/iflytek/astron-agent/pull/926


**Full Changelog**: https://github.com/iflytek/astron-agent/compare/v1.0.1...v1.0.2...
