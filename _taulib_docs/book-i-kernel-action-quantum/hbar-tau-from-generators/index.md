---
{
  "projection_kind": "taulib_declaration",
  "title": "hbar_tau_from_generators",
  "permalink": "/verify/taulib/docs/book-i-kernel-action-quantum/hbar-tau-from-generators/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.ActionQuantum`.",
  "declaration_id": "TauLib.BookI.Kernel.ActionQuantum::hbar_tau_from_generators",
  "declaration_slug": "hbar-tau-from-generators",
  "kind": "theorem",
  "name": "hbar_tau_from_generators",
  "module_name": "TauLib.BookI.Kernel.ActionQuantum",
  "module_url": "/verify/taulib/docs/book-i-kernel-action-quantum/",
  "source_line_start": 69,
  "source_line_end": 70,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/ActionQuantum.lean#L69-L70",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.ActionQuantum",
        "url": "/verify/taulib/docs/book-i-kernel-action-quantum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/ActionQuantum.lean#L69-L70",
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

- Module: [TauLib.BookI.Kernel.ActionQuantum](/verify/taulib/docs/book-i-kernel-action-quantum/)
- Source path: [`TauLib/BookI/Kernel/ActionQuantum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/ActionQuantum.lean#L69-L70)
- Source range: L69-L70
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- ℏ_τ denominator = |generators| − 1. -/
```

## Source Excerpt

```lean
theorem hbar_tau_from_generators : hbar_tau_denom = Generator.all.length - 1 := by
  native_decide
```
