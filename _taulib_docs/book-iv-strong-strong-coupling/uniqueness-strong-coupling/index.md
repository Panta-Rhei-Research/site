---
{
  "projection_kind": "taulib_declaration",
  "title": "UniquenessStrongCoupling",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-coupling/uniqueness-strong-coupling/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongCoupling`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongCoupling::UniquenessStrongCoupling",
  "declaration_slug": "uniqueness-strong-coupling",
  "kind": "structure",
  "name": "UniquenessStrongCoupling",
  "module_name": "TauLib.BookIV.Strong.StrongCoupling",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-coupling/",
  "source_line_start": 126,
  "source_line_end": 135,
  "registry_ids": [
    "IV.T76"
  ],
  "related_registry_items": [
    {
      "id": "IV.T76",
      "title": "Uniqueness of the strong coupling",
      "url": "/registry/object/IV.T76/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L126-L135",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongCoupling",
        "url": "/verify/taulib/docs/book-iv-strong-strong-coupling/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L126-L135",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookIV.Strong.StrongCoupling](/verify/taulib/docs/book-iv-strong-strong-coupling/)
- Source path: [`TauLib/BookIV/Strong/StrongCoupling.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongCoupling.lean#L126-L135)
- Source range: L126-L135
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T76` — Uniqueness of the strong coupling

## Immediate Comment / Docstring

```lean
/-- [IV.T76] Uniqueness of the strong coupling: any tau-admissible
    construction that preserves the strong vacuum, is pi-supported,
    and yields a fixed point of HolEnd_tau(s) must equal alpha_s^*.
    No alternative coupling is consistent with the tau-axioms. -/
```

## Source Excerpt

```lean
structure UniquenessStrongCoupling where
  /-- Unique among admissible constructions. -/
  unique : Bool := true
  /-- Conditions for uniqueness. -/
  condition_vacuum : String := "preserves strong vacuum"
  condition_pi : String := "pi-supported"
  condition_fixed : String := "fixed point of HolEnd_tau(s)"
  /-- No alternatives. -/
  no_alternatives : Bool := true
  deriving Repr
```
