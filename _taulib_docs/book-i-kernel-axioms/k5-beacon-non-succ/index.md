---
{
  "projection_kind": "taulib_declaration",
  "title": "K5_beacon_non_succ",
  "permalink": "/corpus/taulib/docs/book-i-kernel-axioms/k5-beacon-non-succ/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.Axioms`.",
  "declaration_id": "TauLib.BookI.Kernel.Axioms::K5_beacon_non_succ",
  "declaration_slug": "k5-beacon-non-succ",
  "kind": "theorem",
  "name": "K5_beacon_non_succ",
  "module_name": "TauLib.BookI.Kernel.Axioms",
  "module_url": "/corpus/taulib/docs/book-i-kernel-axioms/",
  "source_line_start": 109,
  "source_line_end": 111,
  "registry_ids": [
    "I.K5"
  ],
  "related_registry_items": [
    {
      "id": "I.K5",
      "title": "Beacon Non-Successor (K5)",
      "url": "/registry/object/I.K5/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L109-L111",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Axioms",
        "url": "/corpus/taulib/docs/book-i-kernel-axioms/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L109-L111",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Kernel.Axioms](/corpus/taulib/docs/book-i-kernel-axioms/)
- Source path: [`TauLib/BookI/Kernel/Axioms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L109-L111)
- Source range: L109-L111
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `I.K5` — Beacon Non-Successor (K5)

## Immediate Comment / Docstring

```lean
/-- [I.K5] **Beacon Non-Successor**: ω is NOT in the image of ρ restricted
    to any orbit ray. No finite iteration of ρ on a non-omega generator reaches ω. -/
```

## Source Excerpt

```lean
theorem K5_beacon_non_succ (g : Generator) (hg : g ≠ omega) (n : Nat) :
    (rho ⟨g, n⟩).seed = g := by
  cases g <;> simp [rho] <;> exact absurd rfl hg
```
