---
{
  "projection_kind": "taulib_declaration",
  "title": "example at L126",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-global-hartogs/example-l126/",
  "summary_short": "`example` declaration in `TauLib.BookI.Holomorphy.GlobalHartogs`.",
  "declaration_id": "TauLib.BookI.Holomorphy.GlobalHartogs::#eval:126",
  "declaration_slug": "example-l126",
  "kind": "example",
  "name": null,
  "module_name": "TauLib.BookI.Holomorphy.GlobalHartogs",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-global-hartogs/",
  "source_line_start": 126,
  "source_line_end": 142,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L126-L142",
  "formal_status": "example",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.GlobalHartogs",
        "url": "/verify/taulib/docs/book-i-holomorphy-global-hartogs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L126-L142",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "example",
      "status": "example"
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

- Module: [TauLib.BookI.Holomorphy.GlobalHartogs](/verify/taulib/docs/book-i-holomorphy-global-hartogs/)
- Source path: [`TauLib/BookI/Holomorphy/GlobalHartogs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/GlobalHartogs.lean#L126-L142)
- Source range: L126-L142
- Kind: `example`
- Formal status hint: `example`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Hartogs extends for the identity example at all depths ≤ 5. -/
```

## Source Excerpt

```lean
example : ∀ n k, k ≤ 5 → agree_at id_stage id_stage n k :=
  global_hartogs hartogs_id_example

-- ============================================================
-- SMOKE TESTS
-- ============================================================

-- The four ingredients are all present
#check hartogs_ingredient_spectral
#check hartogs_ingredient_crt
#check hartogs_ingredient_coherence
#check hartogs_ingredient_identity

-- Global Hartogs for concrete example
#check global_hartogs hartogs_id_example

end Tau.Holomorphy
```
