---
{
  "projection_kind": "taulib_declaration",
  "title": "rho_injective",
  "permalink": "/verify/taulib/docs/book-i-kernel-axioms/rho-injective/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.Axioms`.",
  "declaration_id": "TauLib.BookI.Kernel.Axioms::rho_injective",
  "declaration_slug": "rho-injective",
  "kind": "theorem",
  "name": "rho_injective",
  "module_name": "TauLib.BookI.Kernel.Axioms",
  "module_url": "/verify/taulib/docs/book-i-kernel-axioms/",
  "source_line_start": 149,
  "source_line_end": 158,
  "registry_ids": [
    "I.P02"
  ],
  "related_registry_items": [
    {
      "id": "I.P02",
      "title": "rho Injectivity Per Orbit",
      "url": "/registry/object/I.P02/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L149-L158",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L149-L158",
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
- Source path: [`TauLib/BookI/Kernel/Axioms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L149-L158)
- Source range: L149-L158
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P02` — rho Injectivity Per Orbit

## Immediate Comment / Docstring

```lean
/-- [I.P02] ρ is injective on each orbit ray. -/
```

## Source Excerpt

```lean
theorem rho_injective (g : Generator) (hg : g ≠ omega) (n m : Nat) :
    rho ⟨g, n⟩ = rho ⟨g, m⟩ → n = m := by
  intro h
  have h1 := K4_no_jump g hg n
  have h2 := K4_no_jump g hg m
  rw [h1, h2] at h
  cases h
  rfl

end Tau.Kernel
```
