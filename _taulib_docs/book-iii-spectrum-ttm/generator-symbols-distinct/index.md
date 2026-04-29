---
{
  "projection_kind": "taulib_declaration",
  "title": "generator_symbols_distinct",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-ttm/generator-symbols-distinct/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectrum.TTM`.",
  "declaration_id": "TauLib.BookIII.Spectrum.TTM::generator_symbols_distinct",
  "declaration_slug": "generator-symbols-distinct",
  "kind": "theorem",
  "name": "generator_symbols_distinct",
  "module_name": "TauLib.BookIII.Spectrum.TTM",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-ttm/",
  "source_line_start": 263,
  "source_line_end": 275,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L263-L275",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.TTM",
        "url": "/verify/taulib/docs/book-iii-spectrum-ttm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L263-L275",
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

- Module: [TauLib.BookIII.Spectrum.TTM](/verify/taulib/docs/book-iii-spectrum-ttm/)
- Source path: [`TauLib/BookIII/Spectrum/TTM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L263-L275)
- Source range: L263-L275
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The 5 generators are pairwise distinct. -/
```

## Source Excerpt

```lean
theorem generator_symbols_distinct :
    Generator.alpha ≠ Generator.pi ∧
    Generator.alpha ≠ Generator.gamma ∧
    Generator.alpha ≠ Generator.eta ∧
    Generator.alpha ≠ Generator.omega ∧
    Generator.pi ≠ Generator.gamma ∧
    Generator.pi ≠ Generator.eta ∧
    Generator.pi ≠ Generator.omega ∧
    Generator.gamma ≠ Generator.eta ∧
    Generator.gamma ≠ Generator.omega ∧
    Generator.eta ≠ Generator.omega := by
  exact ⟨by decide, by decide, by decide, by decide, by decide,
         by decide, by decide, by decide, by decide, by decide⟩
```
