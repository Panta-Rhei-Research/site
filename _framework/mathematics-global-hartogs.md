---
title: Global Hartogs Extension
module_id: E0-011
layer: E0
strand: holomorphy
summary_short: Boundary determines interior — every τ-holomorphic function extends
  uniquely from the lemniscate.
thesis: The Global Hartogs Extension Theorem proves that omega-tail boundary data
  uniquely determines all finite-stage interior values on τ³.
canonical_books:
- I
source_parts:
- I.16
key_registry:
- I.T31
- I.D65
- I.D66
- I.C02
depends_on:
- E0-010
unlocks:
- E0-012
right_rail:
  related:
  - title: The Earned Topos
    url: /framework/mathematics-earned-topos/
  - title: The Split-Complex Shift
    url: /framework/mathematics-split-complex-shift/
  meta:
    type: Framework Module
    layer: E0 Mathematics
    strand: Holomorphy
    status: Canonical
    updated: April 2026
---

## Overview

*This is the destination.* Every definition, every lemma, every theorem in [Book I]({{ '/publications/books/book-i/' | relative_url }}) was forged for a single purpose: proving that boundary data determines interior values. The Global Hartogs Extension Theorem is the <math><mi>&tau;</mi></math>-analog of Hartogs' classical result (1906) in several complex variables: a holomorphic function defined on the complement of a "thin" set extends uniquely to the entire domain. In the <math><mi>&tau;</mi></math>-framework, this means that omega-tail data on the lemniscate <math><mi>L</mi></math> uniquely determines all finite-stage values on <math><msup><mi>&tau;</mi><mn>3</mn></msup></math>. The boundary governs the interior.

## The Core Idea

A subset <math><mi>K</mi></math> of the lemniscate is **primordially thin** (I.D66) if its primorial projections eventually vanish -- it occupies a negligible fraction of the boundary at every stage. The **Global Hartogs Extension Theorem** (I.T31) states:

> If <math><mi>f</mi></math> is <math><mi>&tau;</mi></math>-holomorphic on <math><mrow><mi>L</mi><mo>&setminus;</mo><mi>K</mi></mrow></math> with <math><mi>K</mi></math> primordially thin, then <math><mi>f</mi></math> extends uniquely to all of <math><mi>L</mi></math>.

No boundedness assumption is required. Thinness alone suffices. This is stronger than the classical Hartogs theorem, which requires dimension <math><mrow><mi>n</mi><mo>&ge;</mo><mn>2</mn></mrow></math> and uses different extension mechanisms (Cauchy integrals, <math><mover><mo>&part;</mo><mo>&macr;</mo></mover></math>-methods). The <math><mi>&tau;</mi></math>-proof uses an entirely different toolkit:

1. **Spectral coefficients** (I.D65): every <math><mrow><mi>f</mi><mo>&in;</mo><mtext>Hol</mtext><mo>(</mo><mi>L</mi><mo>)</mo></mrow></math> has unique spectral coefficients <math><mrow><mo>(</mo><msub><mi>a</mi><mi>k</mi></msub><mo>,</mo><msub><mi>b</mi><mi>k</mi></msub><mo>)</mo></mrow></math> at each primorial stage, decomposed via the lemniscate characters <math><msub><mi>&chi;</mi><mo>+</mo></msub></math> and <math><msub><mi>&chi;</mi><mo>&minus;</mo></msub></math>.

2. **Spectral Determination** (I.T29): a <math><mi>&tau;</mi></math>-holomorphic function is uniquely determined by its spectral coefficients. This is the uniqueness engine.

3. **Restriction map** (I.D66): the canonical map from functions on <math><mi>L</mi></math> to functions on <math><mrow><mi>L</mi><mo>&setminus;</mo><mi>K</mi></mrow></math> is injective (by the [Identity Theorem]({{ '/framework/mathematics-split-complex-holomorphy/' | relative_url }})) and, for thin <math><mi>K</mi></math>, surjective (by the extension theorem). The restriction map is therefore an isomorphism.

4. The proof synthesizes tools from all fifteen preceding Parts: the [earned arithmetic]({{ '/framework/mathematics-earning-arithmetic/' | relative_url }}) (Part III), the ABCD coordinates (Part IV), the [omega-germ]({{ '/framework/mathematics-omega-germs/' | relative_url }}) machinery (Part VII), the [Identity Theorem]({{ '/framework/mathematics-split-complex-holomorphy/' | relative_url }}) (Part XII), and the [earned topos]({{ '/framework/mathematics-earned-topos/' | relative_url }}) structure (Parts XIV-XV).

The central corollary (I.C02) states the principle in its sharpest form: **omega-tail boundary data uniquely determines all finite-stage interior values on <math><msup><mi>&tau;</mi><mn>3</mn></msup></math>.** This is the "boundary determines interior" principle that undergirds the entire physical readout mechanism.

## Why This Matters

The Global Hartogs Extension is the mathematical foundation for the **[Central Theorem]({{ '/framework/mathematics-central-theorem/' | relative_url }})** proved in [Book II]({{ '/publications/books/book-ii/' | relative_url }}): <math><mrow><mi>O</mi><mo>(</mo><msup><mi>&tau;</mi><mn>3</mn></msup><mo>)</mo><mo>&cong;</mo><msub><mi>A</mi><mtext>spec</mtext></msub><mo>(</mo><mi>L</mi><mo>)</mo></mrow></math> -- the space of holomorphic functions on the fibered product is isomorphic to the spectral algebra of the lemniscate. Without the extension theorem, this isomorphism could not be proved: you could not guarantee that boundary data lifts to the interior.

Every physical constant, every prediction, every quantitative claim the framework makes is ultimately a spectral coefficient read from the lemniscate boundary. The Global Hartogs Extension is what makes that reading rigorous.

## Key Claims

1. **I.T31** -- Global Hartogs Extension: holomorphic functions extend past primordially thin sets *(established, machine-checked in [TauLib]({{ '/verify/taulib/' | relative_url }}))*
2. **I.D65** -- Spectral coefficients via lemniscate characters *(established, machine-checked)*
3. **I.T29** -- Spectral Determination: coefficients uniquely determine the function *(established, machine-checked)*
4. **I.C02** -- Boundary determines interior: omega-tail data determines all finite-stage values *(established, machine-checked)*
