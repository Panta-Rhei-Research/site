---
{
  "projection_kind": "taulib_declaration",
  "title": "not_self_containment_pi",
  "permalink": "/corpus/taulib/docs/book-i-sets-orbit-sets/not-self-containment-pi/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.OrbitSets`.",
  "declaration_id": "TauLib.BookI.Sets.OrbitSets::not_self_containment_pi",
  "declaration_slug": "not-self-containment-pi",
  "kind": "theorem",
  "name": "not_self_containment_pi",
  "module_name": "TauLib.BookI.Sets.OrbitSets",
  "module_url": "/corpus/taulib/docs/book-i-sets-orbit-sets/",
  "source_line_start": 162,
  "source_line_end": 164,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L162-L164",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.OrbitSets",
        "url": "/corpus/taulib/docs/book-i-sets-orbit-sets/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L162-L164",
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

- Module: [TauLib.BookI.Sets.OrbitSets](/corpus/taulib/docs/book-i-sets-orbit-sets/)
- Source path: [`TauLib/BookI/Sets/OrbitSets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L162-L164)
- Source range: L162-L164
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.P41c] Type-level separation for π: π_n (as a TauObj) cannot
    appear in Set(π_n), because orbit_set_pi maps TauIdx → Prop
    (it selects α-orbit indices), while π_n = ⟨pi, n⟩ has seed ≠ alpha.

    We formalize this as: for every n, ⟨pi, n⟩.seed ≠ alpha.
    The orbit-set and the original object live in different
    type-level compartments. -/
```

## Source Excerpt

```lean
theorem not_self_containment_pi (n : TauIdx) :
    (⟨pi, n⟩ : TauObj).seed ≠ alpha := by
  simp
```
