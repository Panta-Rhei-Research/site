---
{
  "projection_kind": "taulib_declaration",
  "title": "CINaturality",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/cinaturality/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::CINaturality",
  "declaration_slug": "cinaturality",
  "kind": "structure",
  "name": "CINaturality",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 130,
  "source_line_end": 141,
  "registry_ids": [
    "VII.D66"
  ],
  "related_registry_items": [
    {
      "id": "VII.D66",
      "title": "CI as Naturality Constraint",
      "url": "/registry/object/VII.D66/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L130-L141",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L130-L141",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L130-L141)
- Source range: L130-L141
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D66` — CI as Naturality Constraint

## Immediate Comment / Docstring

```lean
/-- [VII.D66] CI as Naturality Constraint (ch77).
    Site of perspectives (P, J): objects = agent-context perspectives,
    morphisms = admissible reindexings, covers = all relevant viewpoints.
    A maxim M generates presheaf Max_M : P^op → Sets.
    CI satisfied iff Max_M is a natural transformation w.r.t. all
    admissible reindexings. Equivalently: Max_M is a separated presheaf. -/
```

## Source Excerpt

```lean
structure CINaturality where
  /-- Site of perspectives exists. -/
  has_site : Bool := true
  /-- Maxim presheaf Max_M well-defined. -/
  has_maxim_presheaf : Bool := true
  /-- Natural transformation condition. -/
  naturality : Bool := true
  /-- Separated presheaf condition. -/
  separated : Bool := true
  /-- Dignity-filtered: fibers pass through L_dig. -/
  dignity_filtered : Bool := true
  deriving Repr
```
