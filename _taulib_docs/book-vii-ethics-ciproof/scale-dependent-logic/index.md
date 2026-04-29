---
{
  "projection_kind": "taulib_declaration",
  "title": "scale_dependent_logic",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/scale-dependent-logic/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::scale_dependent_logic",
  "declaration_slug": "scale-dependent-logic",
  "kind": "theorem",
  "name": "scale_dependent_logic",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 641,
  "source_line_end": 644,
  "registry_ids": [
    "VII.T23"
  ],
  "related_registry_items": [
    {
      "id": "VII.T23",
      "title": "Scale-Dependent Logic Theorem",
      "url": "/registry/object/VII.T23/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L641-L644",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L641-L644",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L641-L644)
- Source range: L641-L644
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T23` — Scale-Dependent Logic Theorem

## Immediate Comment / Docstring

```lean
/-- [VII.T23] Scale-Dependent Logic (ch39). The logic type is
    determined by the number of NF-addresses in scope:
    - 1 address → Boolean (classical)
    - n addresses → Bayesian (probabilistic)
    - ∞ addresses → Intuitionistic (constructive)
    No single logic is "the" logic; scale determines type. -/
```

## Source Excerpt

```lean
theorem scale_dependent_logic :
    boolean_micro.single_address = true ∧
    bayesian_meso.multi_address = true :=
  ⟨rfl, rfl⟩
```
