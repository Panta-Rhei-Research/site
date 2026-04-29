---
{
  "projection_kind": "taulib_declaration",
  "title": "nat_not_internal_set",
  "permalink": "/verify/taulib/docs/book-i-sets-orbit-sets/nat-not-internal-set/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.OrbitSets`.",
  "declaration_id": "TauLib.BookI.Sets.OrbitSets::nat_not_internal_set",
  "declaration_slug": "nat-not-internal-set",
  "kind": "theorem",
  "name": "nat_not_internal_set",
  "module_name": "TauLib.BookI.Sets.OrbitSets",
  "module_url": "/verify/taulib/docs/book-i-sets-orbit-sets/",
  "source_line_start": 229,
  "source_line_end": 232,
  "registry_ids": [
    "I.R28"
  ],
  "related_registry_items": [
    {
      "id": "I.R28",
      "title": "Inseparability of N and omega",
      "url": "/registry/object/I.R28/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L229-L232",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.OrbitSets",
        "url": "/verify/taulib/docs/book-i-sets-orbit-sets/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L229-L232",
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

- Module: [TauLib.BookI.Sets.OrbitSets](/verify/taulib/docs/book-i-sets-orbit-sets/)
- Source path: [`TauLib/BookI/Sets/OrbitSets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L229-L232)
- Source range: L229-L232
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.R28` — Inseparability of N and omega

## Immediate Comment / Docstring

```lean
/-- [I.R28] Combined "no internal copy" result: for nonzero n, no Set(α_n)
    captures all of ℕ⁺, and Set(ω) strictly exceeds O_α.

    This expresses the inseparability of ℕ and ω: O_α ≅ ℕ⁺ is NOT
    a valid τ-internal set. The closest is Set(ω) = O_α ∪ {ω}. -/
```

## Source Excerpt

```lean
theorem nat_not_internal_set :
    (∀ n : TauIdx, n ≠ 0 → ∃ m : TauIdx, ¬ orbit_set_alpha n m) ∧
    (orbit_set_omega ⟨omega, 0⟩ ∧ (⟨omega, 0⟩ : TauObj).seed ≠ alpha) :=
  ⟨alpha_orbit_set_not_all, omega_orbit_set_exceeds_alpha⟩
```
