---
{
  "projection_kind": "taulib_declaration",
  "title": "h8_admissible_symmetry_synthesis",
  "permalink": "/verify/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/h8-admissible-symmetry-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup`.",
  "declaration_id": "TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup::h8_admissible_symmetry_synthesis",
  "declaration_slug": "h8-admissible-symmetry-synthesis",
  "kind": "theorem",
  "name": "h8_admissible_symmetry_synthesis",
  "module_name": "TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup",
  "module_url": "/verify/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/",
  "source_line_start": 205,
  "source_line_end": 221,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean#L205-L221",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup",
        "url": "/verify/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean#L205-L221",
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

- Module: [TauLib.BookI.KernelFoundation.AdmissibleSymmetryGroup](/verify/taulib/docs/book-i-kernel-foundation-admissible-symmetry-group/)
- Source path: [`TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/KernelFoundation/AdmissibleSymmetryGroup.lean#L205-L221)
- Source range: L205-L221
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 35 H8 admissible-symmetry synthesis**.

    Packages the four-clause structural significance of paper
    §6 Clause (iii):

    1. **Identity is admissible**: `id_admissible : AdmissibleSymmetry`
    2. **Composition closure**: φ ∘ ψ admissible (monoid law)
    3. **Monoid laws**: id-left + id-right + associativity
    4. **NF-invariance**: every admissible symmetry preserves NF

    Together they witness paper §6 Clause (iii) at the
    structural-content level. -/
```

## Source Excerpt

```lean
theorem h8_admissible_symmetry_synthesis (φ ψ : AdmissibleSymmetry)
    (p : Program) :
    -- Clause 1: identity is admissible (acts as id)
    id_admissible.apply p = p ∧
    -- Clause 2: composition is admissible (works pointwise)
    (comp_admissible φ ψ).apply p = φ.apply (ψ.apply p) ∧
    -- Clause 3a: left identity law
    (comp_admissible id_admissible φ).apply p = φ.apply p ∧
    -- Clause 3b: right identity law
    (comp_admissible φ id_admissible).apply p = φ.apply p ∧
    -- Clause 4: NF-invariance (the KEYSTONE)
    normalize (φ.apply p) = normalize p :=
  ⟨id_admissible_apply p,
   comp_admissible_apply φ ψ p,
   id_left_admissible φ p,
   id_right_admissible φ p,
   nf_invariance_under_admissible φ p⟩
```
