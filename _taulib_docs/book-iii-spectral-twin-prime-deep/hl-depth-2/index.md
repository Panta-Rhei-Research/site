---
{
  "projection_kind": "taulib_declaration",
  "title": "hl_depth_2",
  "permalink": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/hl-depth-2/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.TwinPrimeDeep`.",
  "declaration_id": "TauLib.BookIII.Spectral.TwinPrimeDeep::hl_depth_2",
  "declaration_slug": "hl-depth-2",
  "kind": "theorem",
  "name": "hl_depth_2",
  "module_name": "TauLib.BookIII.Spectral.TwinPrimeDeep",
  "module_url": "/corpus/taulib/docs/book-iii-spectral-twin-prime-deep/",
  "source_line_start": 231,
  "source_line_end": 232,
  "registry_ids": [
    "III.D106"
  ],
  "related_registry_items": [
    {
      "id": "III.D106",
      "title": "Hardy-Littlewood Constant",
      "url": "/registry/object/III.D106/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L231-L232",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L231-L232",
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
- Source path: [`TauLib/BookIII/Spectral/TwinPrimeDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/TwinPrimeDeep.lean#L231-L232)
- Source range: L231-L232
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D106` — Hardy-Littlewood Constant

## Immediate Comment / Docstring

```lean
/-- [III.D106] HL constant at depth 2: C₂(2) = 3·1/(2·2) = 3/4. -/
```

## Source Excerpt

```lean
theorem hl_depth_2 :
    hl_twin_constant_approx 2 = (3, 4) := by native_decide
```
