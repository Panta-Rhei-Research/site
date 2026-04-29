---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_atom",
  "permalink": "/verify/taulib/docs/book-i-sets-orbit-sets/prime-atom/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.OrbitSets`.",
  "declaration_id": "TauLib.BookI.Sets.OrbitSets::prime_atom",
  "declaration_slug": "prime-atom",
  "kind": "theorem",
  "name": "prime_atom",
  "module_name": "TauLib.BookI.Sets.OrbitSets",
  "module_url": "/verify/taulib/docs/book-i-sets-orbit-sets/",
  "source_line_start": 183,
  "source_line_end": 191,
  "registry_ids": [
    "I.R30"
  ],
  "related_registry_items": [
    {
      "id": "I.R30",
      "title": "Duality and Atoms",
      "url": "/registry/object/I.R30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L183-L191",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L183-L191",
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
- Source path: [`TauLib/BookI/Sets/OrbitSets.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/OrbitSets.lean#L183-L191)
- Source range: L183-L191
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.R30` — Duality and Atoms

## Immediate Comment / Docstring

```lean
/-- [I.R30] Prime atom theorem: if p is prime, then
    Set(α_p) = {1, p}.
    The only divisors of a prime are 1 and itself. -/
```

## Source Excerpt

```lean
theorem prime_atom (p : TauIdx) (hp : idx_prime p) (k : TauIdx) :
    orbit_set_alpha p k ↔ k = 1 ∨ k = p := by
  simp [orbit_set_alpha_iff_dvd]
  constructor
  · exact hp.2 k
  · intro h
    rcases h with h1 | h2
    · subst h1; exact one_dvd p
    · subst h2; exact dvd_refl k
```
