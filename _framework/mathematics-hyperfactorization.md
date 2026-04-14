---
title: Hyperfactorization Theorem
module_id: E0-005
layer: E0
strand: coordinates
summary_short: Every integer has a unique ABCD decomposition — the first hinge theorem.
thesis: The No-Tie Lemma and Remainder Descent prove that the ABCD encoding is injective;
  coordinate injectivity is the first structural hinge of the series.
canonical_books:
- I
source_parts:
- I.5
key_registry:
- I.T04
- I.L03
- I.L04
depends_on:
- E0-004
unlocks:
- E0-006
right_rail:
  related:
  - title: The ABCD Coordinate Chart
    url: /framework/mathematics-abcd-chart/
  - title: Prime Polarity & the Lemniscate
    url: /framework/mathematics-prime-polarity/
  meta:
    type: Framework Module
    layer: E0 Mathematics
    strand: Coordinates
    status: Canonical
    updated: April 2026
---

## Overview

The [ABCD Coordinate Chart]({{ '/framework/mathematics-abcd-chart/' | relative_url }}) assigns every object a four-dimensional address. But is that address *unique*? The Hyperfactorization Theorem answers: yes. It is the first hinge theorem of the entire series -- the result on which all subsequent structural claims depend. If two distinct objects could share the same ABCD address, the coordinate system would be ambiguous and the framework's later derivations would collapse. The Hyperfactorization Theorem closes that door.

## The Core Idea

The theorem states that every <math><mrow><mi>X</mi><mo>&ge;</mo><mn>2</mn></mrow></math> in <math><mrow><mi>&tau;</mi><mtext>-Idx</mtext></mrow></math> has exactly one decomposition:

<math display="block"><mrow><mi>X</mi><mo>=</mo><msup><mrow><mo>(</mo><mmultiscripts><mi>A</mi><mprescripts/><none/><mi>C</mi></mmultiscripts><mo>)</mo></mrow><mi>B</mi></msup><mo>&sdot;</mo><mi>D</mi></mrow></math>

subject to four conditions: (i) <math><mi>A</mi></math> is an internal prime, (ii) <math><mrow><mi>B</mi><mo>&ge;</mo><mn>1</mn></mrow></math>, (iii) <math><mrow><mi>C</mi><mo>&ge;</mo><mn>1</mn></mrow></math>, and (iv) <math><mrow><mi>D</mi><mo>&ge;</mo><mn>1</mn></mrow></math> with all prime factors of <math><mi>D</mi></math> strictly less than <math><mi>A</mi></math>. Both *existence* and *uniqueness* are proved.

The proof rests on three lemmas, each hard-won:

**Tetration injectivity** (from Part III): if <math><mrow><mmultiscripts><mi>A</mi><mprescripts/><none/><msub><mi>C</mi><mn>1</mn></msub></mmultiscripts><mo>=</mo><mmultiscripts><mi>A</mi><mprescripts/><none/><msub><mi>C</mi><mn>2</mn></msub></mmultiscripts></mrow></math> for prime <math><mi>A</mi></math>, then <math><mrow><msub><mi>C</mi><mn>1</mn></msub><mo>=</mo><msub><mi>C</mi><mn>2</mn></msub></mrow></math>. Tetration preserves enough structural information for the greedy peel to be deterministic.

**The No-Tie Lemma** (I.L03): if both <math><mrow><mmultiscripts><mi>A</mi><mprescripts/><none/><msub><mi>c</mi><mn>1</mn></msub></mmultiscripts><mo>|</mo><mi>X</mi></mrow></math> and <math><mrow><mmultiscripts><mi>A</mi><mprescripts/><none/><msub><mi>c</mi><mn>2</mn></msub></mmultiscripts><mo>|</mo><mi>X</mi></mrow></math> with <math><mrow><msub><mi>c</mi><mn>1</mn></msub><mo>&lt;</mo><msub><mi>c</mi><mn>2</mn></msub></mrow></math>, the greedy algorithm deterministically selects <math><msub><mi>c</mi><mn>2</mn></msub></math>. No two tetration heights can "tie" -- there is always a well-defined maximum. This prevents the coordinate extraction from encountering an ambiguous choice point.

**Strict Remainder Descent** (I.L04): after extracting the tower atom <math><msup><mrow><mo>(</mo><mmultiscripts><mi>A</mi><mprescripts/><none/><mi>C</mi></mmultiscripts><mo>)</mo></mrow><mi>B</mi></msup></math>, the remainder <math><mi>D</mi></math> is strictly smaller in every relevant measure. This ensures the greedy peel terminates and the decomposition is finite.

Together, these three results establish that the ABCD chart <math><mi>&Phi;</mi></math> is not merely total (every object has an address) but *injective* (distinct objects have distinct addresses). The coordinate system is a genuine bijection onto its image.

## Why This Matters

Injectivity has a profound consequence: **shadow equality collapses to ontic identity**. If two objects share the same ABCD coordinates, they are the same object. There is no "accidental" address collision. This means the three-level equality hierarchy introduced in [Earning Arithmetic]({{ '/framework/mathematics-earning-arithmetic/' | relative_url }}) does not produce ghost distinctions -- the coordinate system is faithful to the underlying ontology.

The Hyperfactorization Theorem is called a "hinge" because it is the structural pivot between the kernel's abstract orbit structure and the concrete coordinatized universe that the rest of the framework builds on. The [Prime Polarity Theorem]({{ '/framework/mathematics-prime-polarity/' | relative_url }}) (next module) will use this coordinate system to discover the bipolar structure of primes.

## Key Claims

1. **I.T04** -- Hyperfactorization Theorem: every <math><mrow><mi>X</mi><mo>&ge;</mo><mn>2</mn></mrow></math> has a unique ABCD decomposition *(established, machine-checked in [TauLib]({{ '/verify/taulib/' | relative_url }}))*
2. **I.L03** -- No-Tie Lemma: greedy peel is deterministic *(established, machine-checked)*
3. **I.L04** -- Strict Remainder Descent: decomposition terminates *(established, machine-checked)*
4. Shadow equality collapses to ontic identity under the ABCD chart *(tau-effective)*
