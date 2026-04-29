---
{
  "projection_kind": "taulib_declaration",
  "title": "TTM.run",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-ttm/run/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectrum.TTM`.",
  "declaration_id": "TauLib.BookIII.Spectrum.TTM::TTM.run",
  "declaration_slug": "run",
  "kind": "def",
  "name": "TTM.run",
  "module_name": "TauLib.BookIII.Spectrum.TTM",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-ttm/",
  "source_line_start": 238,
  "source_line_end": 243,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L238-L243",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L238-L243",
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
- Source path: [`TauLib/BookIII/Spectrum/TTM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L238-L243)
- Source range: L238-L243
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Execute up to `fuel` steps. Returns the final configuration. -/
```

## Source Excerpt

```lean
def TTM.run (m : TTM) (c : TTMConfig) (fuel : Nat) : TTMConfig :=
  match fuel with
  | 0 => c
  | fuel' + 1 =>
    if m.isHalted c then c
    else m.run (m.step c) fuel'
```
