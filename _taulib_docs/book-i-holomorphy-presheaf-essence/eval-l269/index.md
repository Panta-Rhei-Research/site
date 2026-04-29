---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L269",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/eval-l269/",
  "summary_short": "`eval` declaration in `TauLib.BookI.Holomorphy.PresheafEssence`.",
  "declaration_id": "TauLib.BookI.Holomorphy.PresheafEssence::#eval:269",
  "declaration_slug": "eval-l269",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookI.Holomorphy.PresheafEssence",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/",
  "source_line_start": 269,
  "source_line_end": 287,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L269-L287",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.PresheafEssence",
        "url": "/verify/taulib/docs/book-i-holomorphy-presheaf-essence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L269-L287",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookI.Holomorphy.PresheafEssence](/verify/taulib/docs/book-i-holomorphy-presheaf-essence/)
- Source path: [`TauLib/BookI/Holomorphy/PresheafEssence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/PresheafEssence.lean#L269-L287)
- Source range: L269-L287
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
#eval (presheaf_of_nat 7).value_at 2     -- 7 % 6 = 1

-- BiSquare type checks
#check chi_plus_bisquare
#check chi_minus_bisquare
#check id_bisquare

-- Crown jewel
#check book_i_crown_jewel

-- Right square automaticity
#check right_from_left chi_plus_bisquare
#check right_from_left' chi_plus_stage chi_plus_coherent

-- Limit principle
#check limit_determines_stages chi_plus_bisquare chi_minus_bisquare
#check limit_determines_spectral

end Tau.Holomorphy
```
