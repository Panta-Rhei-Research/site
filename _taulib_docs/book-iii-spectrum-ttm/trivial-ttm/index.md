---
{
  "projection_kind": "taulib_declaration",
  "title": "trivial_ttm",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-ttm/trivial-ttm/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectrum.TTM`.",
  "declaration_id": "TauLib.BookIII.Spectrum.TTM::trivial_ttm",
  "declaration_slug": "trivial-ttm",
  "kind": "def",
  "name": "trivial_ttm",
  "module_name": "TauLib.BookIII.Spectrum.TTM",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-ttm/",
  "source_line_start": 294,
  "source_line_end": 294,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L294-L294",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.TTM",
        "url": "/verify/taulib/docs/book-iii-spectrum-ttm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L294-L294",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIII.Spectrum.TTM](/verify/taulib/docs/book-iii-spectrum-ttm/)
- Source path: [`TauLib/BookIII/Spectrum/TTM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L294-L294)
- Source range: L294-L294
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A trivial TTM: 1 register, 0 ports, no rules, immediate accept at state 0. -/
```

## Source Excerpt

```lean
def trivial_ttm : TTM := ⟨1, 0, [], 0, [0]⟩
```
