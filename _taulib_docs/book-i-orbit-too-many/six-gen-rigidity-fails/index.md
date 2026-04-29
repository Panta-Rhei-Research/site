---
{
  "projection_kind": "taulib_declaration",
  "title": "six_gen_rigidity_fails",
  "permalink": "/verify/taulib/docs/book-i-orbit-too-many/six-gen-rigidity-fails/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.TooMany`.",
  "declaration_id": "TauLib.BookI.Orbit.TooMany::six_gen_rigidity_fails",
  "declaration_slug": "six-gen-rigidity-fails",
  "kind": "theorem",
  "name": "six_gen_rigidity_fails",
  "module_name": "TauLib.BookI.Orbit.TooMany",
  "module_url": "/verify/taulib/docs/book-i-orbit-too-many/",
  "source_line_start": 139,
  "source_line_end": 144,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooMany.lean#L139-L144",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.TooMany",
        "url": "/verify/taulib/docs/book-i-orbit-too-many/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooMany.lean#L139-L144",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Orbit.TooMany](/verify/taulib/docs/book-i-orbit-too-many/)
- Source path: [`TauLib/BookI/Orbit/TooMany.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/TooMany.lean#L139-L144)
- Source range: L139-L144
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.T09a] **Six-Generator Rigidity Failure**:
    A 6-generator tau-like system admits a non-trivial ρ-automorphism.

    The witness is the swap η ↔ ζ, which:
    (1) commutes with ρ₆ (preserves all dynamical structure)
    (2) is an involution (self-inverse, hence bijective)
    (3) is not the identity (moves ⟨η, 0⟩ to ⟨ζ, 0⟩)

    This shows that adding a 6th generator breaks the rigidity
    property Aut(τ) = {id} that holds for exactly 5 generators. -/
```

## Source Excerpt

```lean
theorem six_gen_rigidity_fails :
    ∃ (f : Obj6 → Obj6),
      (∀ x, f (rho6 x) = rho6 (f x)) ∧
      (∀ x, f (f x) = x) ∧
      ¬(∀ x, f x = x) :=
  ⟨swap6, swap6_rho_comm, swap6_involution, fun h => swap6_ne_id (h _)⟩
```
