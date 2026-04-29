---
{
  "projection_kind": "taulib_declaration",
  "title": "sigmaImpl",
  "permalink": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/sigma-impl/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.ParaconsistentSoundness`.",
  "declaration_id": "TauLib.BookI.Topos.ParaconsistentSoundness::sigmaImpl",
  "declaration_slug": "sigma-impl",
  "kind": "def",
  "name": "sigmaImpl",
  "module_name": "TauLib.BookI.Topos.ParaconsistentSoundness",
  "module_url": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/",
  "source_line_start": 136,
  "source_line_end": 145,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L136-L145",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.ParaconsistentSoundness",
        "url": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L136-L145",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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

- Module: [TauLib.BookI.Topos.ParaconsistentSoundness](/verify/taulib/docs/book-i-topos-paraconsistent-soundness/)
- Source path: [`TauLib/BookI/Topos/ParaconsistentSoundness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L136-L145)
- Source range: L136-L145
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The **σ-implication** on `Truth4 = B_σ`: paper §6.3 Clause (5),
    `φ → ψ ⟧ := σ(⟦ φ ⟧) ∨ ⟦ ψ ⟧`.  Distinct from `Truth4.impl`
    (which uses the diamond-lattice complement `Truth4.neg`); this
    is the paraconsistent implication of the τ-topos's internal
    logic. -/
```

## Source Excerpt

```lean
def sigmaImpl (p q : Truth4) : Truth4 :=
  Truth4.join (sigmaSwap p) q

@[simp] theorem sigmaImpl_T_left (q : Truth4) :
    sigmaImpl T q = q := by
  cases q <;> rfl

@[simp] theorem sigmaImpl_F_left (q : Truth4) :
    sigmaImpl F q = T := by
  cases q <;> rfl
```
