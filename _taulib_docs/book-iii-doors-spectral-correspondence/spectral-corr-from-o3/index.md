---
{
  "projection_kind": "taulib_declaration",
  "title": "spectral_corr_from_O3",
  "permalink": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/spectral-corr-from-o3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Doors.SpectralCorrespondence`.",
  "declaration_id": "TauLib.BookIII.Doors.SpectralCorrespondence::spectral_corr_from_O3",
  "declaration_slug": "spectral-corr-from-o3",
  "kind": "theorem",
  "name": "spectral_corr_from_O3",
  "module_name": "TauLib.BookIII.Doors.SpectralCorrespondence",
  "module_url": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/",
  "source_line_start": 169,
  "source_line_end": 173,
  "registry_ids": [
    "III.T18"
  ],
  "related_registry_items": [
    {
      "id": "III.T18",
      "title": "Spectral Correspondence Theorem",
      "url": "/registry/object/III.T18/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L169-L173",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.SpectralCorrespondence",
        "url": "/verify/taulib/docs/book-iii-doors-spectral-correspondence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L169-L173",
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

- Module: [TauLib.BookIII.Doors.SpectralCorrespondence](/verify/taulib/docs/book-iii-doors-spectral-correspondence/)
- Source path: [`TauLib/BookIII/Doors/SpectralCorrespondence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/SpectralCorrespondence.lean#L169-L173)
- Source range: L169-L173
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T18` — Spectral Correspondence Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T18] Structural: O3 implies finite correspondence at any level. -/
```

## Source Excerpt

```lean
theorem spectral_corr_from_O3 (k : Nat) :
    spectral_correspondence_finite k = true :=
  spectral_correspondence_O3 k

end Tau.BookIII.Doors
```
