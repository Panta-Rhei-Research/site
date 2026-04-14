---
title: Split-Complex Holomorphy
module_id: E0-009
layer: E0
strand: holomorphy
summary_short: D-holomorphic functions with j² = +1 satisfy sector independence; the
  diagonal discipline tames zero divisors.
thesis: τ-holomorphic functions respect split-complex algebra and tower coherence;
  the Identity Theorem restores holomorphic rigidity.
canonical_books:
- I
source_parts:
- I.12
- I.13
key_registry:
- I.D42
- I.T20
- I.T21
- I.T13
depends_on:
- E0-007
unlocks:
- E0-010
- E0-011
right_rail:
  related:
  - title: Omega-Germs & Split-Complex Scalars
    url: /framework/mathematics-omega-germs/
  - title: The Earned Topos
    url: /framework/mathematics-earned-topos/
  - title: Global Hartogs Extension
    url: /framework/mathematics-global-hartogs/
  meta:
    type: Framework Module
    layer: E0 Mathematics
    strand: Holomorphy
    status: Canonical
    updated: April 2026
---

## Overview

Classical complex analysis uses the field <math><mi>&Copf;</mi></math> with <math><mrow><msup><mi>i</mi><mn>2</mn></msup><mo>=</mo><mo>&minus;</mo><mn>1</mn></mrow></math> (elliptic signature). Category <math><mi>&tau;</mi></math> uses the split-complex ring <math><msub><mi>H</mi><mi>&tau;</mi></msub></math> with <math><mrow><msup><mi>j</mi><mn>2</mn></msup><mo>=</mo><mo>+</mo><mn>1</mn></mrow></math> (hyperbolic signature), earned in the [Omega-Germs]({{ '/framework/mathematics-omega-germs/' | relative_url }}) module. In orthodox mathematics, split-complex holomorphy ("D-holomorphy") is considered crippled -- zero divisors (<math><mrow><msub><mi>e</mi><mo>+</mo></msub><mo>&sdot;</mo><msub><mi>e</mi><mo>&minus;</mo></msub><mo>=</mo><mn>0</mn></mrow></math>) seem to destroy the rigidity that makes complex analysis powerful. This module shows how the <math><mi>&tau;</mi></math>-framework rescues D-holomorphy through two structural mechanisms: tower coherence and the diagonal discipline.

## The Core Idea

A function <math><mi>f</mi></math> is **D-differentiable** (I.D42) if it respects the split-complex algebra in its derivative. The **split Cauchy-Riemann equations** (I.D43) carry a plus sign where classical CR equations carry minus -- the hyperbolic signature <math><mrow><msup><mi>j</mi><mn>2</mn></msup><mo>=</mo><mo>+</mo><mn>1</mn></mrow></math> reverses the sign.

In sector coordinates <math><mrow><mo>(</mo><mi>u</mi><mo>,</mo><mi>v</mi><mo>)</mo><mo>=</mo><mo>(</mo><mi>a</mi><mo>+</mo><mi>b</mi><mo>,</mo><mi>a</mi><mo>&minus;</mo><mi>b</mi><mo>)</mo></mrow></math>, the split-CR equations reduce to:

<math display="block"><mrow><mfrac><mrow><mo>&part;</mo><msub><mi>F</mi><mo>+</mo></msub></mrow><mrow><mo>&part;</mo><mi>v</mi></mrow></mfrac><mo>=</mo><mn>0</mn><mo>,</mo><mspace width="20px"/><mfrac><mrow><mo>&part;</mo><msub><mi>F</mi><mo>&minus;</mo></msub></mrow><mrow><mo>&part;</mo><mi>u</mi></mrow></mfrac><mo>=</mo><mn>0</mn></mrow></math>

Each sector component depends on *only one* variable. The **Sector Independence Theorem** (I.P22) formalizes this: every D-holomorphic function decomposes as <math><mrow><mi>f</mi><mo>(</mo><mi>u</mi><mo>,</mo><mi>v</mi><mo>)</mo><mo>=</mo><mo>(</mo><mi>g</mi><mo>(</mo><mi>u</mi><mo>)</mo><mo>,</mo><mi>h</mi><mo>(</mo><mi>v</mi><mo>)</mo><mo>)</mo></mrow></math>. This *is* the wave equation <math><mrow><mfrac><mrow><msup><mo>&part;</mo><mn>2</mn></msup><mi>f</mi></mrow><mrow><mo>&part;</mo><mi>u</mi><mo>&part;</mo><mi>v</mi></mrow></mfrac><mo>=</mo><mn>0</mn></mrow></math> -- a fact with deep physical consequences in the [physics modules]({{ '/framework/physics-hermetic-principle/' | relative_url }}).

The problem with D-holomorphy in orthodox mathematics is that zero divisors destroy uniqueness: many functions can agree on a sector without agreeing globally. The <math><mi>&tau;</mi></math>-framework rescues rigidity through two mechanisms:

1. **Tower coherence**: every <math><mi>&tau;</mi></math>-holomorphic function must be compatible with every primorial reduction map via the CRT. This compatibility condition forces consistency across the entire primorial tower.

2. **Diagonal discipline**: the Object Closure axiom (K5) prevents projecting onto both idempotent sectors simultaneously -- the "diagonal" map that would collapse the two lobes is forbidden.

The crown jewel is the **<math><mi>&tau;</mi></math>-Identity Theorem** (I.T21): if two <math><mi>&tau;</mi></math>-holomorphic functions agree on a sufficiently deep omega-tail, they agree everywhere. The proof uses the **Tail Agreement Propagation** lemma (I.L07): agreement at a single primorial depth propagates upward through the tower. This is the opposite direction from classical analytic continuation (where agreement propagates via Taylor series) -- in <math><mi>&tau;</mi></math>, agreement propagates via CRT coherence.

## Why This Matters

The Identity Theorem restores the full power of holomorphic rigidity to the split-complex setting. Without it, the framework would have functions but no uniqueness theorems -- and without uniqueness, the [boundary-determines-interior]({{ '/framework/mathematics-global-hartogs/' | relative_url }}) principle that underlies the entire physical readout mechanism would fail. This module is the analytic engine that makes the [Central Theorem]({{ '/framework/mathematics-central-theorem/' | relative_url }}) possible.

## Key Claims

1. **I.D42** -- D-differentiability and split Cauchy-Riemann equations *(established, machine-checked in [TauLib]({{ '/verify/taulib/' | relative_url }}))*
2. **I.P22** -- Sector Independence: D-holomorphic functions decompose into independent sector components *(established, machine-checked)*
3. **I.T21** -- <math><mi>&tau;</mi></math>-Identity Theorem: agreement on omega-tails forces global equality *(established, machine-checked)*
4. **I.T13** -- Explosion Barrier: diagonal discipline prevents simultaneous sector projection *(established, machine-checked)*
