---
{
  "projection_kind": "taulib_declaration",
  "title": "twin_admissibility_fraction_5",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/twin-admissibility-fraction-5/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.TwinPrimeDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.TwinPrimeDeep::twin_admissibility_fraction_5",
  "declaration_slug": "twin-admissibility-fraction-5",
  "kind": "theorem",
  "name": "twin_admissibility_fraction_5",
  "module_name": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/",
  "source_line_start": 219,
  "source_line_end": 220,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L219-L220",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L219-L220",
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
- Source path: [`TauLib/BookIII/Spectral/TwinPrimeDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L219-L220)
- Source range: L219-L220
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.P45` — Twin Admissibility Fraction

## Immediate Comment / Docstring

```lean
/-- [III.P45] Admissibility fraction = (p-2)/p for primes 3,5,7,11. -/
```

## Source Excerpt

```lean
theorem twin_admissibility_fraction_5 :
    twin_admissibility_fraction_check 5 = true := by native_decide
```
