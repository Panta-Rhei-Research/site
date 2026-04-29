---
{
  "projection_kind": "taulib_declaration",
  "title": "euler_sieve_cross",
  "permalink": "/verify/taulib/docs/book-i-kernel-action-quantum/euler-sieve-cross/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.ActionQuantum`.",
  "declaration_id": "TauLib.BookI.Kernel.ActionQuantum::euler_sieve_cross",
  "declaration_slug": "euler-sieve-cross",
  "kind": "theorem",
  "name": "euler_sieve_cross",
  "module_name": "TauLib.BookI.Kernel.ActionQuantum",
  "module_url": "/verify/taulib/docs/book-i-kernel-action-quantum/",
  "source_line_start": 109,
  "source_line_end": 110,
  "registry_ids": [
    "I.P44"
  ],
  "related_registry_items": [
    {
      "id": "I.P44",
      "title": "CRT-Galois Decomposition",
      "url": "/registry/object/I.P44/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/ActionQuantum.lean#L109-L110",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/ActionQuantum.lean#L109-L110",
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
- Source path: [`TauLib/BookI/Kernel/ActionQuantum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/ActionQuantum.lean#L109-L110)
- Source range: L109-L110
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P44` — CRT-Galois Decomposition

## Immediate Comment / Docstring

```lean
/-- [I.P44] The Euler sieve identity in cross-multiplied Nat form:
    (2/3) · (4/5) · (121/120) = 121/225

    Cross-multiplied: 2 · 4 · 121 · 225 = 3 · 5 · 120 · 121. -/
```

## Source Excerpt

```lean
theorem euler_sieve_cross :
    2 * 4 * 121 * 225 = 3 * 5 * 120 * (121 : Nat) := by omega
```
