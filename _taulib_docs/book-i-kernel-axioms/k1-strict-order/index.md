---
{
  "projection_kind": "taulib_declaration",
  "title": "K1_strict_order",
  "permalink": "/verify/taulib/docs/book-i-kernel-axioms/k1-strict-order/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.Axioms`.",
  "declaration_id": "TauLib.BookI.Kernel.Axioms::K1_strict_order",
  "declaration_slug": "k1-strict-order",
  "kind": "theorem",
  "name": "K1_strict_order",
  "module_name": "TauLib.BookI.Kernel.Axioms",
  "module_url": "/verify/taulib/docs/book-i-kernel-axioms/",
  "source_line_start": 75,
  "source_line_end": 80,
  "registry_ids": [
    "I.K1"
  ],
  "related_registry_items": [
    {
      "id": "I.K1",
      "title": "Strict Order (K1)",
      "url": "/registry/object/I.K1/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L75-L80",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Axioms",
        "url": "/verify/taulib/docs/book-i-kernel-axioms/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L75-L80",
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

- Module: [TauLib.BookI.Kernel.Axioms](/verify/taulib/docs/book-i-kernel-axioms/)
- Source path: [`TauLib/BookI/Kernel/Axioms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L75-L80)
- Source range: L75-L80
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.K1` — Strict Order (K1)

## Immediate Comment / Docstring

```lean
/-- [I.K1] **Strict Order**: α < π < γ < η < ω is a strict total order
    on the 5 generators.

    In our representation, this holds definitionally via `Generator.toNat`. -/
```

## Source Excerpt

```lean
theorem K1_strict_order :
    alpha.toNat < pi.toNat ∧
    pi.toNat < gamma.toNat ∧
    gamma.toNat < eta.toNat ∧
    eta.toNat < omega.toNat := by
  exact ⟨by decide, by decide, by decide, by decide⟩
```
