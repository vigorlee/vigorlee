<a href="#explore"><img src="assets/header.svg" alt="Mingyi Li — Memory. Reasoning. Motion. Animated perception-to-action loop." width="100%"></a>

<div align="center">

**Embodied AI · Multimodal Reasoning · Robot Navigation**

[Research & projects](#selected-work) · [Interactive explorer](#explore) · [Simulation results](#from-models-to-motion) · [Contact](mailto:limingyi@bit.edu.cn)

<a href="https://github.com/vigorlee?tab=repositories"><img src="https://img.shields.io/github/stars/vigorlee?affiliations=OWNER&amp;style=for-the-badge&amp;label=TOTAL%20STARS&amp;labelColor=142536&amp;color=38bdf8&amp;cacheSeconds=300" alt="Automatically updated total stars received across vigorlee's public repositories"></a> <a href="https://github.com/vigorlee?tab=repositories"><img src="https://img.shields.io/badge/EXPLORE-ALL%20REPOSITORIES-5eead4?style=for-the-badge&amp;labelColor=142536" alt="Explore all repositories"></a>

<sub>Total Stars = stars received across my public repositories, not repositories I have starred. Updated by the badge service; GitHub image caching can delay changes.</sub>

</div>

I build embodied AI systems that connect **multimodal perception → structured memory → grounded decisions → robot execution**. I am with **Beijing Institute of Technology**, working on multimodal retrieval, world-model-assisted autonomy and reproducible robotics.

## Selected work

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/vigorlee/Multimodal--RAG"><img src="assets/emkg.svg" width="100%" alt="EMKG — multimodal memory and retrieval for open-world object-goal navigation"></a><br>
<a href="https://github.com/vigorlee/Multimodal--RAG/stargazers"><img src="https://img.shields.io/github/stars/vigorlee/Multimodal--RAG?style=flat-square&amp;label=Stars&amp;labelColor=142536&amp;color=38bdf8" alt="EMKG live star count"></a>
</td>
<td width="50%" valign="top">
<a href="https://github.com/vigorlee/wave-go"><img src="assets/wave-go.svg" width="100%" alt="WAVE-Go — world-model-assisted Go2-W navigation and verified execution"></a><br>
<a href="https://github.com/vigorlee/wave-go/stargazers"><img src="https://img.shields.io/github/stars/vigorlee/wave-go?style=flat-square&amp;label=Stars&amp;labelColor=142536&amp;color=5eead4" alt="WAVE-Go live star count"></a>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/vigorlee/eidra-agent"><img src="assets/eidra.svg" width="100%" alt="Eidra Agent — persona agents with explicit memory and retrieval"></a><br>
<a href="https://github.com/vigorlee/eidra-agent/stargazers"><img src="https://img.shields.io/github/stars/vigorlee/eidra-agent?style=flat-square&amp;label=Stars&amp;labelColor=142536&amp;color=c4b5fd" alt="Eidra Agent live star count"></a>
</td>
<td width="50%" valign="top">
<a href="https://github.com/vigorlee/lightwheel-kitchen-isaacsim-repro"><img src="assets/simulation.svg" width="100%" alt="Reproducible Lightwheel Kitchen scene for Isaac Sim"></a><br>
<a href="https://github.com/vigorlee/lightwheel-kitchen-isaacsim-repro/stargazers"><img src="https://img.shields.io/github/stars/vigorlee/lightwheel-kitchen-isaacsim-repro?style=flat-square&amp;label=Stars&amp;labelColor=142536&amp;color=f6bd75" alt="Isaac Sim Kitchen live star count"></a>
</td>
</tr>
</table>

## Explore

**Choose a direction — click to open. / 点击展开，探索我的研究方向。**

<details>
<summary><b>01 · How can a robot remember what it sees? / 感知与记忆</b></summary>

### From observations to useful memory

I explore semantic-spatial memory and multimodal retrieval for open-world object-goal navigation: visual observations become evidence that a robot can retrieve and use when choosing where to go.

**Explore:** [EMKG / Multimodal RAG](https://github.com/vigorlee/Multimodal--RAG)

`Multimodal RAG` · `ObjectNav` · `Vision-language models` · `Structured memory`

</details>

<details>
<summary><b>02 · How do model decisions become robot motion? / 决策与执行</b></summary>

### From a high-level task to verified execution

WAVE-Go connects world-model-assisted decisions with navigation and Go2-W control. Its two workflows cover map-independent charging and hybrid long-range navigation. In the latter, Cosmos3-Edge chooses an approved route; Nav2/RoamerX handles navigation, and DreamWaQ controls motion.

**Explore:** [WAVE-Go](https://github.com/vigorlee/wave-go) · [Three-scenario simulation evidence](https://github.com/vigorlee/wave-go/tree/main/demos/go2w-cosmos-extended-navigation/evidence/2026-09-10)

`World models` · `Robot navigation` · `Go2-W` · `Verified execution`

</details>

<details>
<summary><b>03 · How can agent memory stay inspectable? / 智能体与可复现性</b></summary>

### Make memory and experiments easier to inspect

Eidra Agent explores explicit memory, retrieval and adversarial smoke tests for persona agents. My simulation work also focuses on scripted setup, asset checks and clear validation evidence.

**Explore:** [Eidra Agent](https://github.com/vigorlee/eidra-agent) · [Isaac Sim Kitchen](https://github.com/vigorlee/lightwheel-kitchen-isaacsim-repro) · [Room runtime](https://github.com/vigorlee/Room)

`Agent memory` · `Retrieval` · `Isaac Sim` · `Reproducible experiments`

</details>

## From models to motion

<a href="https://github.com/vigorlee/wave-go#三类场景实录"><img src="https://raw.githubusercontent.com/vigorlee/wave-go/6b3cc9658b7e9ebbb22beec3420c674a08907f27/demos/go2w-cosmos-extended-navigation/evidence/2026-09-10/overview.jpg" width="100%" alt="WAVE-Go verified simulation: Go2-W ascends and descends physical ramps while passing center-course cylinders"></a>

**18/18 stages · 60.88 m · 3 scenario types** — stairs, ramps, and flat-ground obstacles with moving cylinder proxies. Recorded in MuJoCo / Unreal Engine on September 10, 2026. These are simulation results with sensor/model-fused obstacle data, not a real-robot benchmark.

[Inspect the results →](https://github.com/vigorlee/wave-go/tree/main/demos/go2w-cosmos-extended-navigation/evidence/2026-09-10)

---

<div align="center">

**Clear boundaries. Reproducible setup. Inspectable evidence.**

Beijing Institute of Technology · [limingyi@bit.edu.cn](mailto:limingyi@bit.edu.cn) · [All repositories](https://github.com/vigorlee?tab=repositories)

<sub>Built with GitHub-native expandable sections, clickable project cards and an animated SVG. [How the live statistics work](PROFILE.md).</sub>

</div>
