---
{
  "projection_kind": "taulib_declaration",
  "title": "orbit_set_alpha",
  "permalink": "/verify/taulib/docs/book-i-sets-orbit-sets/orbit-set-alpha/",
  "summary_short": "`def` declaration in `TauLib.BookI.Sets.OrbitSets`.",
  "declaration_id": "TauLib.BookI.Sets.OrbitSets::orbit_set_alpha",
  "declaration_slug": "orbit-set-alpha",
  "kind": "def",
  "name": "orbit_set_alpha",
  "module_name": "TauLib.BookI.Sets.OrbitSets",
  "module_url": "/verify/taulib/docs/book-i-sets-orbit-sets/",
  "source_line_start": 58,
  "source_line_end": 66,
  "registry_ids": [
    "I.D94"
  ],
  "related_registry_items": [
    {
      "id": "I.D94",
      "title": "Orbit-Set Map",
      "url": "/registry/object/I.D94/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L58-L66",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L58-L66",
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

- Module: [TauLib.BookI.Sets.OrbitSets](/verify/taulib/docs/book-i-sets-orbit-sets/)
- Source path: [`TauLib/BookI/Sets/OrbitSets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L58-L66)
- Source range: L58-L66
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D94` — Orbit-Set Map

## Immediate Comment / Docstring

```lean
/-- [I.D94] Set(α_n): the divisor set = τ-membership.
    α_k ∈ Set(α_n) iff tau_mem k n (iff k | n).

    This IS τ-membership (I.D31) — the orbit-set for α and the
    internal membership relation are the same concept. We define
    orbit_set_alpha in terms of tau_mem to enforce this identity. -/
```

## Source Excerpt

```lean
def orbit_set_alpha (n : TauIdx) (k : TauIdx) : Prop := tau_mem k n

/-- Simp lemma: orbit_set_alpha unfolds to Nat divisibility for proofs. -/
@[simp] theorem orbit_set_alpha_iff_dvd (n k : TauIdx) :
    orbit_set_alpha n k ↔ k ∣ n :=
  tau_mem_iff_dvd k n

noncomputable instance instDecidableOrbitSetAlpha (n k : TauIdx) :
    Decidable (orbit_set_alpha n k) := Classical.dec _
```
