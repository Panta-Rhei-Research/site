---
title: Prime Polarity & the Lemniscate
module_id: E0-006
layer: E0
strand: boundary
summary_short: Primes induce bipolar polarization; the ensemble yields the algebraic
  lemniscate L = S¹ ∨ S¹.
thesis: The CRT decomposition of the profinite boundary ring produces two independent
  sectors whose reunion is the lemniscate — geometry earned from arithmetic.
canonical_books:
- I
source_parts:
- I.6
key_registry:
- I.T05
- I.D37
- I.D38
depends_on:
- E0-005
unlocks:
- E0-007
right_rail:
  related:
  - title: Hyperfactorization Theorem
    url: /framework/mathematics-hyperfactorization/
  - title: Omega-Germs & Split-Complex Scalars
    url: /framework/mathematics-omega-germs/
  meta:
    type: Framework Module
    layer: E0 Mathematics
    strand: Boundary
    status: Canonical
    updated: April 2026
---

## Overview

The second hinge theorem of the series. Once the [Hyperfactorization Theorem]({{ '/framework/mathematics-hyperfactorization/' | relative_url }}) proves that every object has a unique ABCD address, the framework asks: what structural pattern do the primes carry? The answer is unexpectedly geometric: every prime is either *B-dominant* (gamma-polar) or *C-dominant* (eta-polar), and both classes are infinite. This bipolar partition is a purely number-theoretic result -- yet its consequence is the algebraic lemniscate <math><mrow><mi>L</mi><mo>=</mo><msup><mi>S</mi><mn>1</mn></msup><mo>&or;</mo><msup><mi>S</mi><mn>1</mn></msup></mrow></math>, a figure-eight curve that becomes the boundary of the framework's entire geometric structure. Geometry is earned from arithmetic alone.

## The Core Idea

For each internal prime <math><mi>p</mi></math>, the **spectral signature** examines the population of objects where <math><mi>p</mi></math> appears as the dominant tower atom. Two patterns emerge:

- **B-dominant** (gamma-polar) primes: the exponent channel dominates. The prime "prefers" exponential growth over tetration growth.
- **C-dominant** (eta-polar) primes: the tetration channel dominates. The symmetric condition holds.

The **Prime Polarity Theorem** (I.T05) proves that every prime falls into exactly one class -- there is no third option, and no prime is neutral. Both classes are infinite.

The geometric consequence emerges through the **Chinese Remainder Theorem** applied to the profinite boundary ring. The CRT decomposition separates the ring of boundary functions into two independent sectors -- one for each polarity class. These two sectors define the algebraic lemniscate (I.D37): two lobes meeting at a single crossing point (I.D38) where the two sectors share their identity element.

This is not a metaphor. The lemniscate is a *theorem* -- derived from the arithmetic of the [coherence kernel]({{ '/framework/mathematics-coherence-kernel/' | relative_url }}) with no geometric axioms, no embedding in Euclidean space, and no imported topology. The two lobes correspond to the two polarity classes.

## Why This Matters

The lemniscate <math><mi>L</mi></math> becomes the **boundary** of the entire framework -- the surface on which holomorphic functions are evaluated, physical constants are read out, and the [Central Theorem]({{ '/framework/mathematics-central-theorem/' | relative_url }}) is stated. Every physical prediction the framework makes is ultimately a readout from this lemniscate. The fact that <math><mi>L</mi></math> is *earned* from the primes is one of the most distinctive features of the program.

The [Omega-Germs]({{ '/framework/mathematics-omega-germs/' | relative_url }}) module will show how this lemniscate structure produces the split-complex scalar ring.

## Key Claims

1. **I.T05** -- Prime Polarity Theorem: every prime is B-dominant or C-dominant, both infinite *(established, machine-checked in [TauLib]({{ '/verify/taulib/' | relative_url }}))*
2. **I.D37** -- Algebraic lemniscate earned from CRT decomposition *(established, machine-checked)*
3. **I.D38** -- Crossing-point germ at the lemniscate node *(established, machine-checked)*
4. Geometry earned from pure number theory with no geometric axioms *(tau-effective)*
