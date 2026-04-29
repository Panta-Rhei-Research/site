---
{
  "projection_kind": "taulib_declaration",
  "title": "tetration_ge_arg",
  "permalink": "/verify/taulib/docs/book-i-polarity-spectral/tetration-ge-arg/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.Spectral`.",
  "declaration_id": "TauLib.BookI.Polarity.Spectral::tetration_ge_arg",
  "declaration_slug": "tetration-ge-arg",
  "kind": "theorem",
  "name": "tetration_ge_arg",
  "module_name": "TauLib.BookI.Polarity.Spectral",
  "module_url": "/verify/taulib/docs/book-i-polarity-spectral/",
  "source_line_start": 81,
  "source_line_end": 87,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Spectral.lean#L81-L87",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.Spectral",
        "url": "/verify/taulib/docs/book-i-polarity-spectral/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Spectral.lean#L81-L87",
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

- Module: [TauLib.BookI.Polarity.Spectral](/verify/taulib/docs/book-i-polarity-spectral/)
- Source path: [`TauLib/BookI/Polarity/Spectral.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/Spectral.lean#L81-L87)
- Source range: L81-L87
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Tetration grows at least as fast as the argument: a↑↑c ≥ c for a ≥ 2. -/
```

## Source Excerpt

```lean
theorem tetration_ge_arg (a : Nat) (ha : a ≥ 2) (c : Nat) :
    tetration a c ≥ c := by
  induction c with
  | zero => simp [tetration]
  | succ c ih =>
    have := tetration_strict_mono a ha c
    omega
```
