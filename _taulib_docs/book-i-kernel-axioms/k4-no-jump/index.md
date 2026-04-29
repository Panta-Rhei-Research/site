---
{
  "projection_kind": "taulib_declaration",
  "title": "K4_no_jump",
  "permalink": "/verify/taulib/docs/book-i-kernel-axioms/k4-no-jump/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.Axioms`.",
  "declaration_id": "TauLib.BookI.Kernel.Axioms::K4_no_jump",
  "declaration_slug": "k4-no-jump",
  "kind": "theorem",
  "name": "K4_no_jump",
  "module_name": "TauLib.BookI.Kernel.Axioms",
  "module_url": "/verify/taulib/docs/book-i-kernel-axioms/",
  "source_line_start": 103,
  "source_line_end": 105,
  "registry_ids": [
    "I.K4"
  ],
  "related_registry_items": [
    {
      "id": "I.K4",
      "title": "No-Jump / Cover (K4)",
      "url": "/registry/object/I.K4/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L103-L105",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L103-L105",
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
- Source path: [`TauLib/BookI/Kernel/Axioms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L103-L105)
- Source range: L103-L105
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.K4` — No-Jump / Cover (K4)

## Immediate Comment / Docstring

```lean
/-- [I.K4] **No-Jump / Cover**: ρ acts as a successor within each orbit
    (no skipping). The cover relation is immediate: ρⁿ(g) covers ρⁿ⁻¹(g). -/
```

## Source Excerpt

```lean
theorem K4_no_jump (g : Generator) (hg : g ≠ omega) (n : Nat) :
    rho ⟨g, n⟩ = ⟨g, n + 1⟩ := by
  cases g <;> simp [rho] <;> exact absurd rfl hg
```
