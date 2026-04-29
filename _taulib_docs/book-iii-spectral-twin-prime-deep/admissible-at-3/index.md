---
{
  "projection_kind": "taulib_declaration",
  "title": "admissible_at_3",
  "permalink": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/admissible-at-3/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.TwinPrimeDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.TwinPrimeDeep::admissible_at_3",
  "declaration_slug": "admissible-at-3",
  "kind": "theorem",
  "name": "admissible_at_3",
  "module_name": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "module_url": "/verify/taulib/docs/book-iii-spectral-twin-prime-deep/",
  "source_line_start": 243,
  "source_line_end": 244,
  "registry_ids": [
    "III.P45"
  ],
  "related_registry_items": [
    {
      "id": "III.P45",
      "title": "Twin Admissibility Fraction",
      "url": "/registry/object/III.P45/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L243-L244",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L243-L244",
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
- Source path: [`TauLib/BookIII/Spectral/TwinPrimeDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L243-L244)
- Source range: L243-L244
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P45` — Twin Admissibility Fraction

## Immediate Comment / Docstring

```lean
/-- [III.P45] At prime 3: 1 out of 3 admissible (3-2=1). -/
```

## Source Excerpt

```lean
theorem admissible_at_3 :
    count_admissible_at_prime 3 = 1 := by native_decide
```
