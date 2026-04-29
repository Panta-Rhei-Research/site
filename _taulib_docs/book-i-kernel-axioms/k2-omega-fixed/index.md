---
{
  "projection_kind": "taulib_declaration",
  "title": "K2_omega_fixed",
  "permalink": "/verify/taulib/docs/book-i-kernel-axioms/k2-omega-fixed/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.Axioms`.",
  "declaration_id": "TauLib.BookI.Kernel.Axioms::K2_omega_fixed",
  "declaration_slug": "k2-omega-fixed",
  "kind": "theorem",
  "name": "K2_omega_fixed",
  "module_name": "TauLib.BookI.Kernel.Axioms",
  "module_url": "/verify/taulib/docs/book-i-kernel-axioms/",
  "source_line_start": 85,
  "source_line_end": 87,
  "registry_ids": [
    "I.K2"
  ],
  "related_registry_items": [
    {
      "id": "I.K2",
      "title": "Omega Fixed Point (K2)",
      "url": "/registry/object/I.K2/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L85-L87",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L85-L87",
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
- Source path: [`TauLib/BookI/Kernel/Axioms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L85-L87)
- Source range: L85-L87
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.K2` — Omega Fixed Point (K2)

## Immediate Comment / Docstring

```lean
/-- [I.K2] **Omega Fixed Point**: ρ(ω) = ω; ω absorbs all operations.

    This holds definitionally from our `rho` definition. -/
```

## Source Excerpt

```lean
theorem K2_omega_fixed (n : Nat) :
    rho ⟨omega, n⟩ = ⟨omega, n⟩ := by
  simp [rho]
```
