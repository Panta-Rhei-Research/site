---
{
  "projection_kind": "taulib_declaration",
  "title": "SpectralSatisfiable",
  "permalink": "/corpus/taulib/docs/book-iii-spectrum-three-sat/spectral-satisfiable/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectrum.ThreeSAT`.",
  "declaration_id": "TauLib.BookIII.Spectrum.ThreeSAT::SpectralSatisfiable",
  "declaration_slug": "spectral-satisfiable",
  "kind": "def",
  "name": "SpectralSatisfiable",
  "module_name": "TauLib.BookIII.Spectrum.ThreeSAT",
  "module_url": "/corpus/taulib/docs/book-iii-spectrum-three-sat/",
  "source_line_start": 119,
  "source_line_end": 120,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L119-L120",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.ThreeSAT",
        "url": "/corpus/taulib/docs/book-iii-spectrum-three-sat/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L119-L120",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookIII.Spectrum.ThreeSAT](/corpus/taulib/docs/book-iii-spectrum-three-sat/)
- Source path: [`TauLib/BookIII/Spectrum/ThreeSAT.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/ThreeSAT.lean#L119-L120)
- Source range: L119-L120
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A CNF is spectrally satisfiable if there exists a value v such that
    spectral_cnf evaluates to true. -/
```

## Source Excerpt

```lean
def SpectralSatisfiable (φ : CNF) : Prop :=
  ∃ v : TauIdx, spectral_cnf φ v = true
```
