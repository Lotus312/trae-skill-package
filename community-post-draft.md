#trae技巧便利店

我想分享一个自己在真实项目里反复打磨出来的 Skill：`clean-code-web-game`。

它不是一个“大而全”的通用提示词，而是一套专门服务于 Web Game 重构的工作流。背景很简单：游戏项目一旦进入迭代期，最容易出现的问题不是“功能写不出来”，而是“越改越不敢动”。尤其是 Phaser 这类项目，`scene / store / renderer / config` 一旦职责混在一起，后面每次改一个关卡、加一个变体、补一个交互，都很容易把旧玩法带坏。

我做这个 Skill 的目的，就是把自己在项目里反复验证过的做法固定下来：先识别真正的坏味道，再定义哪些玩法行为不能变，然后按最小步重构，把共享流程和关卡专属表现拆开，最后用 build 和自动化回归兜底。

## 适用场景

- Phaser 或其他 Canvas/Web Game 项目
- 多个 Scene / 多个关卡变体并存
- 一个文件里同时混了共享流程和关卡专属逻辑
- 想按 Clean Code 整理结构，但不想因为“重构洁癖”打坏玩法

## 我是怎么用它的

这个 Skill 的使用方式很直接，输入重构任务，它会输出一份结构化的重构 brief，包括：

- 先检查哪些高风险坏味道
- 推荐的重构顺序
- 默认的职责拆分边界
- 重构时的 guardrails
- 最低限度的验证清单

例如：

```bash
python3 main.py \
  --task "Refactor a level scene that mixes V01 and V02 logic" \
  --target "src/phaser/VoyageLevelScene.ts"
```

它不会一上来就鼓励“抽象一切”，而是会优先提示：

- 先把共享场景壳和关卡专属 renderer 拆开
- 把 progression / judgement / scoring 留在 store 或 runtime
- 把 copy / threshold / level rules 留在 config
- 每改完一步，都要跑构建和行为回归

## 这个 Skill 是怎么写出来的

我不是先看官方模板再倒推内容，而是先在项目里真的做了一轮重构，再把有效的方法沉淀成 Skill。

这套方法在我的项目里主要做了几件事：

- 把一个混合 `V01 / V02` 逻辑的关卡 Scene 拆成共享 shell + 独立 renderer
- 把 `GameStore` 里的运行时、解锁推进、结果快照、调试快照逐层拆出去
- 把地图面板状态、节点视觉状态、HUD 文案都改成纯 helper
- 重构过程中始终用 build 和自动化回归兜底

所以这个 Skill 的核心不是“写得花”，而是“在真实项目里确实有用”。

## 我觉得它最有价值的地方

我现在越来越觉得，很多时候最适合自己的 Skill，不是社区最热门的那个，而是你自己在项目里一遍遍试出来、知道哪里最容易翻车之后，才真正打磨出来的那个。

`clean-code-web-game` 对我来说就是这样一个 Skill。它不是为了追求抽象，而是为了在游戏项目里更稳地做结构治理。

如果你也在做 Phaser 或其他 Web Game 项目，欢迎拿去改成适合自己项目的版本。

## 附件

- GitHub: https://github.com/Lotus312/clean-code-web-game-skill
- 标准化 ZIP 包：可直接附上 `clean-code-web-game-trae.zip`

如果发帖时我会再补两张图：

- 重构前：一个 Scene 混多个关卡逻辑
- 重构后：共享 Scene 壳 + renderer / store / config 分层
