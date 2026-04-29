---
{
  "projection_kind": "taulib_declaration",
  "title": "IsDesignated",
  "permalink": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/is-designated/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.ParaconsistentSoundness`.",
  "declaration_id": "TauLib.BookI.Topos.ParaconsistentSoundness::IsDesignated",
  "declaration_slug": "is-designated",
  "kind": "def",
  "name": "IsDesignated",
  "module_name": "TauLib.BookI.Topos.ParaconsistentSoundness",
  "module_url": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/",
  "source_line_start": 106,
  "source_line_end": 120,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L106-L120",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L106-L120",
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
- Source path: [`TauLib/BookI/Topos/ParaconsistentSoundness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L106-L120)
- Source range: L106-L120
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The designated sector** of `Truth4 = B_σ`
    (paper Def 6.4.i): `D = {T, B} = {e_+, 1}`, the Belnap–Dunn
    "truths and near-truths."  A formula is valid at a valuation
    iff its interpretation lands in `D`. -/
```

## Source Excerpt

```lean
def IsDesignated : Truth4 → Prop
  | T => True
  | B => True
  | F => False
  | N => False

@[simp] theorem isDesignated_T : IsDesignated T := trivial
@[simp] theorem isDesignated_B : IsDesignated B := trivial
@[simp] theorem not_isDesignated_F : ¬ IsDesignated F := id
@[simp] theorem not_isDesignated_N : ¬ IsDesignated N := id

/-- Designation is decidable on `Truth4` (4-element finite-state
    check). -/
instance : DecidablePred IsDesignated := fun v => by
  cases v <;> simp [IsDesignated] <;> infer_instance
```
