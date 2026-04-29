---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_no_full_resonance",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/tau-no-full-resonance/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.MetaLogic.DiagonalResonance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.DiagonalResonance::tau_no_full_resonance",
  "declaration_slug": "tau-no-full-resonance",
  "kind": "theorem",
  "name": "tau_no_full_resonance",
  "module_name": "TauLib.BookI.MetaLogic.DiagonalResonance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/",
  "source_line_start": 66,
  "source_line_end": 66,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L66-L66",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.DiagonalResonance",
        "url": "/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L66-L66",
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

- Module: [TauLib.BookI.MetaLogic.DiagonalResonance](/verify/taulib/docs/book-i-meta-logic-diagonal-resonance/)
- Source path: [`TauLib/BookI/MetaLogic/DiagonalResonance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/DiagonalResonance.lean#L66-L66)
- Source range: L66-L66
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- τ does NOT exhibit full diagonal resonance. -/
```

## Source Excerpt

```lean
theorem tau_no_full_resonance : tau_resonance.isFullResonance = false := by native_decide
```
