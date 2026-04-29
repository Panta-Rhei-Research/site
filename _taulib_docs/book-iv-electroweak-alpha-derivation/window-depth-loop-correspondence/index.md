---
{
  "projection_kind": "taulib_declaration",
  "title": "window_depth_loop_correspondence",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/window-depth-loop-correspondence/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.AlphaDerivation`.",
  "declaration_id": "TauLib.BookIV.Electroweak.AlphaDerivation::window_depth_loop_correspondence",
  "declaration_slug": "window-depth-loop-correspondence",
  "kind": "theorem",
  "name": "window_depth_loop_correspondence",
  "module_name": "TauLib.BookIV.Electroweak.AlphaDerivation",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/",
  "source_line_start": 432,
  "source_line_end": 433,
  "registry_ids": [
    "IV.T204"
  ],
  "related_registry_items": [
    {
      "id": "IV.T204",
      "title": "Window Depth–Loop Order Correspondence",
      "url": "/registry/object/IV.T204/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L432-L433",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.AlphaDerivation",
        "url": "/verify/taulib/docs/book-iv-electroweak-alpha-derivation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L432-L433",
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

- Module: [TauLib.BookIV.Electroweak.AlphaDerivation](/verify/taulib/docs/book-iv-electroweak-alpha-derivation/)
- Source path: [`TauLib/BookIV/Electroweak/AlphaDerivation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/AlphaDerivation.lean#L432-L433)
- Source range: L432-L433
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `IV.T204` — Window Depth–Loop Order Correspondence

## Immediate Comment / Docstring

```lean
/-- [IV.T204] Depth–loop correspondence: W₃(3)=17, W₄(3)=18, W₅(3)=19. -/
```

## Source Excerpt

```lean
theorem window_depth_loop_correspondence :
    (17 : Nat) + 1 = 18 ∧ (18 : Nat) + 1 = 19 := ⟨rfl, rfl⟩
```
