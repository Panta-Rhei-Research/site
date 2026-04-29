---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_decidable",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-three-sat/spectral-decidable/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectrum.ThreeSAT`.",
  "declaration_id": "TauLib.BookIII.Spectrum.ThreeSAT::spectral_decidable",
  "declaration_slug": "spectral-decidable",
  "kind": "theorem",
  "name": "spectral_decidable",
  "module_name": "TauLib.BookIII.Spectrum.ThreeSAT",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-three-sat/",
  "source_line_start": 129,
  "source_line_end": 131,
  "registry_ids": [
    "I.P31"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L129-L131",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.ThreeSAT",
        "url": "/verify/taulib/docs/book-iii-spectrum-three-sat/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L129-L131",
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

- Module: [TauLib.BookIII.Spectrum.ThreeSAT](/verify/taulib/docs/book-iii-spectrum-three-sat/)
- Source path: [`TauLib/BookIII/Spectrum/ThreeSAT.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L129-L131)
- Source range: L129-L131
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.P31] The spectral encoding is decidable: for any formula and
    value, we can compute whether the formula is spectrally satisfied.
    This is the computable core of the encoding. -/
```

## Source Excerpt

```lean
theorem spectral_decidable (φ : CNF) (v : TauIdx) :
    spectral_cnf φ v = true ∨ spectral_cnf φ v = false := by
  cases spectral_cnf φ v <;> simp
```
