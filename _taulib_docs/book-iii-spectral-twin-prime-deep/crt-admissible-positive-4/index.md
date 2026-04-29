---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_admissible_positive_4",
  "permalink": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/crt-admissible-positive-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.TwinPrimeDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.TwinPrimeDeep::crt_admissible_positive_4",
  "declaration_slug": "crt-admissible-positive-4",
  "kind": "theorem",
  "name": "crt_admissible_positive_4",
  "module_name": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/",
  "source_line_start": 215,
  "source_line_end": 216,
  "registry_ids": [
    "III.T75"
  ],
  "related_registry_items": [
    {
      "id": "III.T75",
      "title": "CRT Admissible Positive",
      "url": "/registry/object/III.T75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L215-L216",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.TwinPrimeDeep",
        "url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L215-L216",
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

- Module: [TauLib.BookIII.Spectral.TwinPrimeDeep](/verify/taulib/docs/book-iii-spectral-twin-prime-deep/)
- Source path: [`TauLib/BookIII/Spectral/TwinPrimeDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L215-L216)
- Source range: L215-L216
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.T75` — CRT Admissible Positive

## Immediate Comment / Docstring

```lean
/-- [III.T75] CRT-admissible residues positive at depths 1..4. -/
```

## Source Excerpt

```lean
theorem crt_admissible_positive_4 :
    crt_admissible_positive_check 4 = true := by native_decide
```
