---
{
  "projection_kind": "taulib_declaration",
  "title": "TauZero",
  "permalink": "/verify/taulib/docs/book-i-kernel-signature/tau-zero/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Kernel.Signature`.",
  "declaration_id": "TauLib.BookI.Kernel.Signature::TauZero",
  "declaration_slug": "tau-zero",
  "kind": "structure",
  "name": "TauZero",
  "module_name": "TauLib.BookI.Kernel.Signature",
  "module_url": "/verify/taulib/docs/book-i-kernel-signature/",
  "source_line_start": 98,
  "source_line_end": 104,
  "registry_ids": [
    "I.D04"
  ],
  "related_registry_items": [
    {
      "id": "I.D04",
      "title": "Static Kernel tau_0",
      "url": "/registry/object/I.D04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Signature.lean#L98-L104",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Signature",
        "url": "/verify/taulib/docs/book-i-kernel-signature/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Signature.lean#L98-L104",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookI.Kernel.Signature](/verify/taulib/docs/book-i-kernel-signature/)
- Source path: [`TauLib/BookI/Kernel/Signature.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Signature.lean#L98-L104)
- Source range: L98-L104
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.D04` — Static Kernel tau_0

## Immediate Comment / Docstring

```lean
/-- [I.D04] The static kernel τ₀: the 5 generators before the generative act.
    This is the complete specification — ρ has not yet been applied. -/
```

## Source Excerpt

```lean
structure TauZero where
  /-- The five generators are present -/
  generators : Fin 5 → Generator
  /-- They are listed in canonical order -/
  canonical_order : ∀ i j : Fin 5, i < j → (generators i).toNat < (generators j).toNat

end Tau.Kernel
```
