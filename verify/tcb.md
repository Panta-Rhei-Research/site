---
layout: program-doc
title: "Trust Budget and TCB Disclosure"
permalink: /verify/tcb/
lane: verify
summary_short: "The trust budget: what Lean's kernel trusts, and what TauLib extends it by. TauLib uses `native_decide` in approximately 1,800 places — including the Book II Central Theorem — which extends the trusted computing base beyond Lean's kernel to include `Lean.ofReduceBool` and `Lean.trustCompiler`. This page discloses that cost, locates it, and explains why it is accepted."
right_rail:
  related:
    - title: "Release Manifest"
      url: /verify/release-manifest/
    - title: "Custom Axiom Inventory"
      url: /verify/custom-axioms/
    - title: "Formalization Status"
      url: /verify/taulib/status/
    - title: "Formal Methods Audit"
      url: /verify/how-to-audit/formal-methods/
  meta:
    type: "Trust Disclosure"
    scope: "TauLib TCB extensions"
    status: "Canonical"
    updated: "April 2026"
---

The trust budget: what Lean's kernel trusts, and what TauLib extends it by.

A framework that claims "machine-checked in Lean 4" owes the reader a precise statement of what "machine-checked" means here, because Lean 4 — like every proof assistant — has a trusted computing base (TCB) that sits under every theorem. Theorems in TauLib that rely on `native_decide` extend that TCB in a specific, named way. This page discloses that extension.

## Kernel baseline

Lean 4's kernel trusts the Calculus of Inductive Constructions (CIC) and its standard axioms (`propext`, `Quot.sound`, `Classical.choice`). That is the irreducible baseline: every Lean theorem ultimately bottoms out at the kernel accepting a term of the claimed type, using only CIC reduction and those axioms.

The kernel is what has been audited over years of community use, what large projects like Mathlib have stress-tested, and what formal-methods reviewers refer to when they speak of "trusted by Lean." No non-trivial theorem in any Lean library avoids extending the kernel's baseline — every project's question is *how much* and *where*.

## The `native_decide` extension

TauLib uses `native_decide` in approximately **1,824 places** across the library, including, load-bearingly, the **Book II Central Theorem** (`central_theorem_3_15`).

Any reader can check the TCB cost at the Lean REPL:

```lean
#print axioms central_theorem_3_15
```

The output includes, beyond the Mathlib baseline (`Classical.choice`, `propext`, `Quot.sound`):

- **`Lean.ofReduceBool`** — trusts that Lean's definitional reduction of a `Bool`-valued expression to `true` commutes with kernel-level equality. Specifically: if the compiled `Bool`-valued check returns `true`, the kernel accepts this as a witness that the proposition holds.
- **`Lean.trustCompiler`** — trusts Lean's native compilation pipeline to produce a correct executable from a Lean definition. The `native_decide` tactic runs the compiled version of a decidable check; `Lean.trustCompiler` is the axiom that says that compiled run is faithful to the source.

Together, these extend TauLib's TCB from "Lean's kernel alone" to **"Lean's kernel plus the native compiler pipeline."**

This is the framework's honest disclosure: the Book II Central Theorem's proof chain leans on the correctness of Lean's native compiler and on the `ofReduceBool` axiom. A reviewer who does not accept either extension should treat the Central Theorem (and every theorem in the list below) as conditionally verified.

## Why we accept this tradeoff

Finite `Bool`-valued checks of the kinds TauLib uses are intractable for kernel-only reduction in reasonable build time. Concretely:

- **Central Theorem at rank (3, 15).** The algebraic check at that rank involves a finite but large finite computation over the window-algebra integers. Kernel-only `decide` would exceed build-time limits by orders of magnitude.
- **Window-algebra integers W_n(k).** Verification of closed-form identities at bounded (n, k) pairs — including the load-bearing W₃(4) = 5 and W₅(3) = 19 — uses `native_decide` on the same grounds.
- **Axiom finite-envelopes.** Each of the three conjectural axioms in Book III ships with a paired `*_finite_check` theorem verifying the universal claim holds at all configurations up to a stated bound. These checks run via `native_decide`.

`native_decide` is used *deliberately* where the kernel-only `decide` would not terminate in minutes. The alternative — writing out the finite check as a kernel-reducible proof term — produces objects that exceed Lean's kernel memory envelope before completing. That is a hard engineering limit, not a shortcut.

## Which theorems depend on `native_decide`

The following theorems, when inspected with `#print axioms`, surface `Lean.ofReduceBool` and `Lean.trustCompiler` in their axiom chain:

| Theorem | Module | Why `native_decide` |
|---------|--------|---------------------|
| `central_theorem_3_15` | `BookII.Central.Theorem` | Finite check of the ring isomorphism at rank (3,15) |
| `bridge_ledger_check` | `BookIII.Bridge.BridgeAxiom` | Finite-envelope check paired with the bridge functor axiom |
| `spectral_correspondence_O3_check` | `BookIII.Doors.SpectralCorrespondence` | Finite-envelope check for the O(3) spectral axiom |
| `grand_grh_adelic_check` | `BookIII.Doors.GrandGRH` | Finite-envelope check for the Grand GRH axiom |
| `consecutive_window_integers` | `BookIV.Arena` | Closed-form check on W_n(k) closed-form identities |
| `physics_ledger_consistency` (V.T101) | `BookV.Physics.Ledger` | Numerical consistency of derived constants |

This is a partial list; the full enumeration of theorems whose `#print axioms` output includes the TCB extension will be published as a CI-generated artifact in a future release (see closing note).

## Which theorems don't

The following theorems, when inspected with `#print axioms`, surface **only** the Mathlib baseline — no `Lean.ofReduceBool`, no `Lean.trustCompiler`:

| Theorem | Module | Proof style |
|---------|--------|-------------|
| `rigidity_non_omega` | `BookI.Kernel.Rigidity` | Structural induction on kernel axioms K0–K6 |
| `categoricity_non_omega` | `BookI.Kernel.Categoricity` | Categorical uniqueness argument, kernel-reducible |
| `categorical_imperative_fixed_point` | `BookVII.Ethics.Imperative` | Fixed-point argument on the commitment lattice; kernel-reducible |
| `modal_S4_theorem` (VII.T13) | `BookVII.Logos.ModalOperators` | Syntactic S4 derivation |

A reviewer who wants to restrict attention to theorems that use no `native_decide` can start from this list and trace the dependency graph outward.

## The three conjectural axioms and their finite checks

Each of the three custom axioms in TauLib (all in Book III — see [Custom Axiom Inventory]({{ '/verify/custom-axioms/' | relative_url }})) ships paired with a finite-envelope `native_decide` check. The axiom asserts the universal claim; the paired check verifies the claim holds at all configurations up to a stated bound. The check's TCB cost is the `native_decide` extension disclosed on this page; the axiom's TCB cost is the axiom itself.

| # | Axiom | Module | TCB cost |
|---|-------|--------|----------|
| 1 | `bridge_functor_exists` | `BookIII/Bridge/BridgeAxiom.lean` | The universal claim (axiom); a finite envelope check via `native_decide` is included, which adds `Lean.ofReduceBool` + `Lean.trustCompiler` |
| 2 | `spectral_correspondence_O3` | `BookIII/Doors/SpectralCorrespondence.lean` | Same pattern: universal axiom plus paired `native_decide` finite check |
| 3 | `grand_grh_adelic` | `BookIII/Doors/GrandGRH.lean` | Same pattern: universal axiom plus paired `native_decide` finite check |

A reviewer who accepts Lean's kernel but not the native compiler pipeline should treat the paired finite checks as "not yet verified at this TCB level." The universal axioms remain axioms regardless of the finite-check TCB — they are the step the framework declines to prove.

## What a reviewer should do with this disclosure

1. **Run `#print axioms` on the theorems you care about.** The output is authoritative; the tables on this page are a guide, not a replacement.
2. **Decide whether to accept the `native_decide` extension.** A Lean 4 reviewer who has audited the compiler pipeline may accept it; one who has not may wish to rebuild the load-bearing finite checks at kernel-level, accepting the build-time cost.
3. **Separate the two kinds of cost.** The three Book III axioms are *mathematical* commitments — the universal step the framework declines to prove. The `native_decide` extension is an *engineering* commitment — that Lean's native compiler is faithful. These are independent; accepting one does not require accepting the other.

## Why this page exists

This disclosure is the posture we prefer: name the cost, locate it, let the reader decide whether to take it on.

A prior version of the Verify lane warned auditors about `native_decide` as a red flag on audit checklists — while the headline theorem of Book II was itself proved by it. That was an inconsistency. It is now corrected: the `native_decide` usage is disclosed in full, the theorems that depend on it are enumerated, and the reader is given the tools to make their own determination.

A future release will report per-theorem `#print axioms` output as a CI-generated artifact linked from each registry entry, so that the TCB footprint of any claim is a single click away rather than requiring a local Lean 4 build. Until then, the disclosure on this page plus a local `lake build` at the pinned commit is the reproducible protocol.

## Cross-links

- [Release Manifest]({{ '/verify/release-manifest/' | relative_url }}) — pinned commit, overall axiom and `sorry` inventory
- [Custom Axiom Inventory]({{ '/verify/custom-axioms/' | relative_url }}) — the three Book III axioms in detail
- [Formalization Status]({{ '/verify/taulib/status/' | relative_url }}) — per-book statistics
- [Formal Methods Audit Route]({{ '/verify/how-to-audit/formal-methods/' | relative_url }}) — step-by-step verification protocol
- [Scope Labels]({{ '/verify/taulib/scope-labels/' | relative_url }}) — how conjectural-axiom dependencies propagate through the registry
