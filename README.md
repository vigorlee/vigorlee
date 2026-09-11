# Mingyi Li

Beijing Institute of Technology

[Email](mailto:limingyi@bit.edu.cn) · [Repositories](https://github.com/vigorlee?tab=repositories)

My research interests lie in embodied intelligence, with a focus on multimodal memory, retrieval-augmented reasoning, and robot navigation. I study how perceptual observations can be represented and retrieved to support decision-making in embodied systems.

## Research interests

- **Multimodal representation and memory:** semantic and spatial representations for open-world environments.
- **Embodied reasoning and navigation:** connecting high-level decisions with navigation and robot execution.
- **Reproducible systems:** experimental infrastructure for studying agent memory and robotic simulation.

## Selected projects

### [EMKG / Multimodal RAG](https://github.com/vigorlee/Multimodal--RAG)

Multimodal knowledge graph integration for open-world object-goal navigation. This project investigates the use of structured memory and multimodal retrieval to support navigation decisions.

<details>
<summary>Research focus</summary>

Visual observations are organized into semantic-spatial memory that can be queried during navigation. The work concerns the connection between environmental observations, retrieved evidence, and object-goal decisions.

[Source code and project documentation](https://github.com/vigorlee/Multimodal--RAG)

</details>

### [WAVE-Go](https://github.com/vigorlee/wave-go)

World-model-assisted navigation and execution for the Go2-W platform, including map-independent charging and hybrid long-range navigation workflows.

<details>
<summary>System details and experimental materials</summary>

In the hybrid navigation workflow, Cosmos3-Edge selects an approved route, Nav2/RoamerX handles navigation, and DreamWaQ controls motion.

The September 10, 2026 simulation record covers stairs, ramps, and flat-ground obstacles with moving cylinder proxies. It reports 18 completed stages and 60.88 m of travel in MuJoCo / Unreal Engine, using sensor/model-fused obstacle data. These results describe the recorded simulation runs, rather than a real-robot benchmark.

[Experimental records](https://github.com/vigorlee/wave-go/tree/main/demos/go2w-cosmos-extended-navigation/evidence/2026-09-10) · [Simulation overview](https://raw.githubusercontent.com/vigorlee/wave-go/6b3cc9658b7e9ebbb22beec3420c674a08907f27/demos/go2w-cosmos-extended-navigation/evidence/2026-09-10/overview.jpg)

</details>

### [Eidra Agent](https://github.com/vigorlee/eidra-agent)

An experimental framework for persona agents with explicit memory and retrieval, with adversarial smoke tests for inspecting agent behavior.

<details>
<summary>Related infrastructure</summary>

[Isaac Sim Kitchen](https://github.com/vigorlee/lightwheel-kitchen-isaacsim-repro) provides a reproducible Lightwheel Kitchen scene setup. [Room](https://github.com/vigorlee/Room) contains related runtime work. These repositories support scripted setup, asset checks, and experimental inspection.

</details>

---

[![Total repository stars](https://img.shields.io/github/stars/vigorlee?affiliations=OWNER&style=flat&label=Total%20repository%20stars&labelColor=555555&color=737373&cacheSeconds=300)](https://github.com/vigorlee?tab=repositories)

<sub>Current stars received across public repositories owned by this account. Automatically updated by the badge service; GitHub image caching may delay changes.</sub>
