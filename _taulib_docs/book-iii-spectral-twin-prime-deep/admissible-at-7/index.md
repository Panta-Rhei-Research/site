---
{
  "projection_kind": "taulib_declaration",
  "title": "admissible_at_7",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/admissible-at-7/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.TwinPrimeDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.TwinPrimeDeep::admissible_at_7",
  "declaration_slug": "admissible-at-7",
  "kind": "theorem",
  "name": "admissible_at_7",
  "module_name": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/",
  "source_line_start": 251,
  "source_line_end": 252,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L251-L252",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.TwinPrimeDeep",
        "url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L251-L252",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIII.Spectral.TwinPrimeDeep](/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/)
- Source path: [`TauLib/BookIII/Spectral/TwinPrimeDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L251-L252)
- Source range: L251-L252
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.P45` — Twin Admissibility Fraction

## Immediate Comment / Docstring

```lean
/-- [III.P45] At prime 7: 5 out of 7 admissible (7-2=5). -/
```

## Source Excerpt

```lean
theorem admissible_at_7 :
    count_admissible_at_prime 7 = 5 := by native_decide
```
