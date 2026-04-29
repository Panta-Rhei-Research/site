---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_plus_crt_complexity",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-interface-width/chi-plus-crt-complexity/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectrum.InterfaceWidth`.",
  "declaration_id": "TauLib.BookIII.Spectrum.InterfaceWidth::chi_plus_crt_complexity",
  "declaration_slug": "chi-plus-crt-complexity",
  "kind": "theorem",
  "name": "chi_plus_crt_complexity",
  "module_name": "TauLib.BookIII.Spectrum.InterfaceWidth",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-interface-width/",
  "source_line_start": 134,
  "source_line_end": 136,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L134-L136",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.InterfaceWidth",
        "url": "/verify/taulib/docs/book-iii-spectrum-interface-width/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L134-L136",
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

- Module: [TauLib.BookIII.Spectrum.InterfaceWidth](/verify/taulib/docs/book-iii-spectrum-interface-width/)
- Source path: [`TauLib/BookIII/Spectrum/InterfaceWidth.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L134-L136)
- Source range: L134-L136
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- τ-admissible functions have finite CRT complexity:
    χ₊ depends only on n mod M_k at stage k. -/
```

## Source Excerpt

```lean
theorem chi_plus_crt_complexity (n k : TauIdx) :
    chi_plus_stage.b_fun n k = chi_plus_stage.b_fun (reduce n k) k := by
  simp [chi_plus_stage, reduce, Nat.mod_mod_of_dvd n (dvd_refl (primorial k))]
```
