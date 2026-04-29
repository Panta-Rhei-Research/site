---
{
  "projection_kind": "taulib_declaration",
  "title": "sdual_exponent_large",
  "permalink": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/sdual-exponent-large/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Spectral.ConfinementBridge`.",
  "declaration_id": "TauLib.BookIII.Spectral.ConfinementBridge::sdual_exponent_large",
  "declaration_slug": "sdual-exponent-large",
  "kind": "theorem",
  "name": "sdual_exponent_large",
  "module_name": "TauLib.BookIII.Spectral.ConfinementBridge",
  "module_url": "/verify/taulib/docs/book-iii-spectral-confinement-bridge/",
  "source_line_start": 194,
  "source_line_end": 196,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L194-L196",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L194-L196",
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
- Source path: [`TauLib/BookIII/Spectral/ConfinementBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/ConfinementBridge.lean#L194-L196)
- Source range: L194-L196
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The S-dual imaginary part 1/ι_τ is large.
    2π/ι_τ > 18 because 2π > 6.28 and 1/ι_τ > 2.93, product > 18.
    Cross-multiplied: 18 · ι_τ < 2π, i.e., 18 · 341304 < 2π · 10⁶.
    We use 2π > 6283185/10⁶ (conservative).

    2π · 10⁶ > 6283185 and 18 · 341304 = 6143472.
    So 6283185 > 6143472 ✓ -/
```

## Source Excerpt

```lean
theorem sdual_exponent_large :
    18 * iota < 6283185 := by
  simp [iota, iota_tau_numer]
```
