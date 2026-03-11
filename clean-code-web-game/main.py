#!/usr/bin/env python3
import argparse
import json
import sys

SMELLS = [
    "A single file mixes shared gameplay flow and level-specific presentation.",
    "A scene owns both runtime truth and visual updates.",
    "Thresholds, labels, and layout constants are duplicated across files.",
    "A switch or branch tree keeps growing for level/layout variants.",
    "Editing one level keeps regressing another level.",
    "Naming hides intent, such as temp/data2/handleThing-style identifiers."
]

RULES = [
    "Keep gameplay timing, pass/fail rules, unlock logic, and visible flow unchanged unless behavior changes are explicitly requested.",
    "Prefer moving level-specific visuals into dedicated renderers before touching shared runtime logic.",
    "Keep shared orchestration in one place and push variant-specific code outward.",
    "Prefer explicit names over clever abstractions when levels look similar but evolve differently.",
    "Delete clearly unused code when regression checks already protect behavior."
]

BOUNDARIES = [
    "Scene: lifecycle, input wiring, high-level composition, shared HUD.",
    "Renderer/Layout: per-level visuals and layout updates.",
    "Store/Runtime: judgement, progression, scoring, unlocks, save-related state.",
    "Content/Config: copy, thresholds, counts, and level-specific rules."
]

CHECKS = [
    "Build succeeds.",
    "Type checks succeed if the project has them.",
    "Existing gameplay regression checks still pass.",
    "If visuals changed, inspect a real screenshot rather than only debug text."
]


def build_brief(task: str, target: str, stack: str) -> str:
    target_line = target if target else "Not specified"
    lines = [
        "# Clean Code Web Game Brief",
        "",
        "## Request",
        f"- Task: {task}",
        f"- Target: {target_line}",
        f"- Stack: {stack}",
        "",
        "## Refactor Goal",
        "- Improve structure without breaking gameplay, progression, or player-visible timing.",
        "",
        "## Smells To Check First",
    ]
    lines.extend(f"- {item}" for item in SMELLS)
    lines.extend(
        [
            "",
            "## Recommended Refactor Order",
            "1. Identify the real smell instead of refactoring for aesthetics alone.",
            "2. Define the behavior that must not change.",
            "3. Pick the smallest refactor that removes one smell class.",
            "4. Separate shared orchestration from level-specific visuals.",
            "5. Verify after each meaningful change.",
            "",
            "## Default Boundary Split",
        ]
    )
    lines.extend(f"- {item}" for item in BOUNDARIES)
    lines.extend(
        [
            "",
            "## Guardrails",
        ]
    )
    lines.extend(f"- {item}" for item in RULES)
    lines.extend(
        [
            "",
            "## Verification",
        ]
    )
    lines.extend(f"- {item}" for item in CHECKS)
    lines.extend(
        [
            "",
            "## Output Expectation",
            "- Smaller responsibility surfaces.",
            "- Clearer names.",
            "- Fewer cross-level regressions.",
            "- A refactor that can be explained in 2-4 concrete points."
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a clean-code refactor brief for a web game project."
    )
    parser.add_argument("--task", required=True, help="Refactor task description.")
    parser.add_argument("--target", default="", help="Primary file or module.")
    parser.add_argument(
        "--stack",
        default="Phaser/Vite web game",
        help="Engine or project stack context."
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format."
    )
    args = parser.parse_args()

    if args.format == "json":
        payload = {
            "task": args.task,
            "target": args.target or None,
            "stack": args.stack,
            "smells": SMELLS,
            "rules": RULES,
            "boundaries": BOUNDARIES,
            "verification": CHECKS
        }
        json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 0

    print(build_brief(args.task, args.target, args.stack))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
