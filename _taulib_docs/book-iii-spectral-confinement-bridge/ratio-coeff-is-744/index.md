---
{
  "projection_kind": "taulib_declaration",
  "title": "ratio_coeff_is_744",
  "permalink": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/ratio-coeff-is-744/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.ConfinementBridge`.",
  "declaration_id": "TauLib.BookIII.Spectral.ConfinementBridge::ratio_coeff_is_744",
  "declaration_slug": "ratio-coeff-is-744",
  "kind": "theorem",
  "name": "ratio_coeff_is_744",
  "module_name": "TauLib.BookIII.Spectral.ConfinementBridge",
  "module_url": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/",
  "source_line_start": 230,
  "source_line_end": 230,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L230-L230",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.ConfinementBridge",
        "url": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L230-L230",
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

- Module: [TauLib.BookIII.Spectral.ConfinementBridge](/verify/taulib/docs/book-iii-spectral-confinement-bridge/)
- Source path: [`TauLib/BookIII/Spectral/ConfinementBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L230-L230)
- Source range: L230-L230
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The ratio coefficient 744 = 240 + 504 = constant term of j-invariant. -/
```

## Source Excerpt

```lean
theorem ratio_coeff_is_744 : (240 : Nat) + 504 = 744 := by omega
```
