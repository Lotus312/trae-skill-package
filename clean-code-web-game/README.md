# clean-code-web-game

一个面向 Web Game 重构场景的 Skill 包，重点不是“把代码写得更抽象”，而是按 Clean Code 原则整理结构，同时尽量不打坏玩法、关卡流程和自动化回归。

## 适用场景

- Phaser 或其他 Canvas/Web Game 项目
- 有多个 Scene、多个关卡变体，或者共享一套游戏 UI 的项目
- `scene / runtime / renderer / config` 职责已经开始混杂
- 你想做结构治理，但又不想因为重构把玩法改坏

## 这个 Skill 解决什么问题

它会根据输入的任务描述，输出一份结构化的重构 brief，内容包括：

- 先检查哪些高风险坏味道
- 推荐的重构顺序
- 默认的职责拆分边界
- 重构时不能踩的坑
- 最低限度的验证清单

## 文件结构

```text
clean-code-web-game/
├── skill.json
├── main.py
└── README.md
```

## 使用方法

示例 1：针对一个混合了多个关卡视觉分支的 Scene 文件生成重构 brief

```bash
python3 main.py \
  --task "Refactor a level scene that mixes V01 and V02 logic" \
  --target "src/phaser/VoyageLevelScene.ts"
```

示例 2：输出 JSON，方便再接到别的工作流里

```bash
python3 main.py \
  --task "Clean up store logic without breaking level progression" \
  --target "src/game/GameStore.ts" \
  --format json
```

## 编写思路

这个 Skill 来自一个真实 Phaser 节奏游戏项目的重构过程。核心经验不是“追求绝对优雅”，而是：

- 先定义玩法哪些行为绝对不能变
- 先拆共享流程和关卡专属表现
- 每次只收一类坏味道
- 每次改完都做构建和行为回归

## 分享建议

如果你把它发到社区，可以重点讲这几个点：

- 这个 Skill 不是通用提示词堆砌，而是项目里反复验证过的工作流
- 重点价值是“提结构，不打坏玩法”
- 特别适合 Phaser/Web Game 这种一改结构就容易出回归的项目
