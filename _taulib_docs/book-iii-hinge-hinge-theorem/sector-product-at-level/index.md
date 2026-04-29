---
{
  "projection_kind": "taulib_declaration",
  "title": "sector_product_at_level",
  "permalink": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/sector-product-at-level/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Hinge.HingeTheorem`.",
  "declaration_id": "TauLib.BookIII.Hinge.HingeTheorem::sector_product_at_level",
  "declaration_slug": "sector-product-at-level",
  "kind": "def",
  "name": "sector_product_at_level",
  "module_name": "TauLib.BookIII.Hinge.HingeTheorem",
  "module_url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/",
  "source_line_start": 73,
  "source_line_end": 78,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L73-L78",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Hinge.HingeTheorem",
        "url": "/verify/taulib/docs/book-iii-hinge-hinge-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L73-L78",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookIII.Hinge.HingeTheorem](/verify/taulib/docs/book-iii-hinge-hinge-theorem/)
- Source path: [`TauLib/BookIII/Hinge/HingeTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Hinge/HingeTheorem.lean#L73-L78)
- Source range: L73-L78
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Sector product at an enrichment level: the layer template determines
    which sectors are active at each level. -/
```

## Source Excerpt

```lean
def sector_product_at_level (lev : EnrLevel) (k : TauIdx) : TauIdx :=
  match lev with
  | .E0 => sector_product .B k * sector_product .C k * sector_product .Omega k
  | .E1 => sector_product .B k * sector_product .C k
  | .E2 => sector_product .D k * sector_product .A k
  | .E3 => 1  -- metaphysics: products collapse to unity (self-model)
```
