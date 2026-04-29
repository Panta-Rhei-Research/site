---
{
  "projection_kind": "taulib_declaration",
  "title": "bridge_functor_exists",
  "permalink": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/bridge-functor-exists/",
  "summary_short": "`axiom` declaration in `TauLib.BookIII.Bridge.BridgeAxiom`.",
  "declaration_id": "TauLib.BookIII.Bridge.BridgeAxiom::bridge_functor_exists",
  "declaration_slug": "bridge-functor-exists",
  "kind": "axiom",
  "name": "bridge_functor_exists",
  "module_name": "TauLib.BookIII.Bridge.BridgeAxiom",
  "module_url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/",
  "source_line_start": 134,
  "source_line_end": 135,
  "registry_ids": [
    "III.D71"
  ],
  "related_registry_items": [
    {
      "id": "III.D71",
      "title": "Bridge Axiom",
      "url": "/registry/object/III.D71/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L134-L135",
  "formal_status": "axiom",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.BridgeAxiom",
        "url": "/verify/taulib/docs/book-iii-bridge-bridge-axiom/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L134-L135",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "axiom",
      "status": "axiom"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIII.Bridge.BridgeAxiom](/verify/taulib/docs/book-iii-bridge-bridge-axiom/)
- Source path: [`TauLib/BookIII/Bridge/BridgeAxiom.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/BridgeAxiom.lean#L134-L135)
- Source range: L134-L135
- Kind: `axiom`
- Formal status hint: `axiom`

## Registry Links

- `III.D71` — Bridge Axiom

## Immediate Comment / Docstring

```lean
/-- [III.D71] **CONJECTURE-AXIOM — CONDITIONAL RESULTS DOWNSTREAM**

    Bridge functor existence for all `(bound, db)`. This is one of
    exactly three conjecture-axioms in TauLib; see also
    `spectral_correspondence_O3` (`BookIII.Doors.SpectralCorrespondence`)
    and `grand_grh_adelic` (`BookIII.Doors.GrandGRH`).

    **Conjectural scope.** At finite level,
    `bridge_functor_check bound db` is decidable and verifies the
    finite shadow of the bridge functor for every parameter pair
    `(bound, db)` with `bound ≤ 15` and `db ≤ 3` — hundreds of
    discrete checks, each closed in the kernel by `native_decide`.
    This axiom asserts that the finite check extends to the full
    universal statement `∀ bound db`. That extension is the
    conjectural content.

    **Downstream theorems are CONDITIONAL RESULTS.** Any theorem in
    TauLib whose transitive proof chain invokes `bridge_functor_exists`
    is conditional on the universal extension of the finite
    `bridge_functor_check`. Running `#print axioms <theorem-name>` on
    a downstream theorem will list `bridge_functor_exists` among its
    trusted assumptions — this is exactly the audit trail a Lean
    reader should expect, and it is what makes the conditional
    status of downstream results inspectable rather than hidden.

    **Preferred encoding (future work).** The Mathlib-community
    idiom for a conjectural dependency is to take the assumption as
    an explicit hypothesis on each downstream theorem rather than as
    a global axiom. Refactoring the downstream Book III theorems to
    take `bridge_functor_exists` (or a `(h : BridgeFunctorExists)`
    binder) as a hypothesis is planned for a future wave; this
    would make `#print axioms` reveal no unexplained axioms on
    unconditional theorems. Until then, the global `axiom`
    declaration is the encoding. -/
```

## Source Excerpt

```lean
axiom bridge_functor_exists :
  ∀ bound db : TauIdx, bridge_functor_check bound db = true
```
