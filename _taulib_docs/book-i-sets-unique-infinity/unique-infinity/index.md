---
{
  "projection_kind": "taulib_declaration",
  "title": "unique_infinity",
  "permalink": "/verify/taulib/docs/book-i-sets-unique-infinity/unique-infinity/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.UniqueInfinity`.",
  "declaration_id": "TauLib.BookI.Sets.UniqueInfinity::unique_infinity",
  "declaration_slug": "unique-infinity",
  "kind": "theorem",
  "name": "unique_infinity",
  "module_name": "TauLib.BookI.Sets.UniqueInfinity",
  "module_url": "/verify/taulib/docs/book-i-sets-unique-infinity/",
  "source_line_start": 115,
  "source_line_end": 140,
  "registry_ids": [
    "I.T36"
  ],
  "related_registry_items": [
    {
      "id": "I.T36",
      "title": "Unique Infinity Object",
      "url": "/registry/object/I.T36/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L115-L140",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.UniqueInfinity",
        "url": "/verify/taulib/docs/book-i-sets-unique-infinity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L115-L140",
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

- Module: [TauLib.BookI.Sets.UniqueInfinity](/verify/taulib/docs/book-i-sets-unique-infinity/)
- Source path: [`TauLib/BookI/Sets/UniqueInfinity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L115-L140)
- Source range: L115-L140
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T36` — Unique Infinity Object

## Immediate Comment / Docstring

```lean
/-- [I.T36] Unique Infinity Object: omega is the ONLY infinity object
    in Category tau.

    Proof: Let x be any infinity object. Since rho(x) = x and x is
    unreachable from orbit rays, x must have seed = omega (by K6
    object closure, the only objects not in orbit rays have seed omega).
    Then x = (omega, d) for some d. Since rho(omega, d) = (omega, d)
    (K2), ANY omega-seeded object is rho-fixed.

    But the uniqueness is stronger: all (omega, d) are rho-equivalent
    (they all satisfy rho(x) = x), so up to rho-equivalence there is
    exactly one infinity object. -/
```

## Source Excerpt

```lean
theorem unique_infinity (x : TauObj) (hx : InfinityObject x) :
    x.seed = omega := by
  -- By K6 object closure, x.seed is one of the 5 generators
  rcases K6_object_closure x with h | h | h | h | h
  · -- seed = alpha: then rho(x) = (alpha, x.depth + 1) != x
    exfalso
    have hrho := hx.rho_fixed
    rw [show x = ⟨alpha, x.depth⟩ from by cases x; simp at h; simp [h]] at hrho
    simp [rho] at hrho
  · -- seed = pi: same argument
    exfalso
    have hrho := hx.rho_fixed
    rw [show x = ⟨pi, x.depth⟩ from by cases x; simp at h; simp [h]] at hrho
    simp [rho] at hrho
  · -- seed = gamma
    exfalso
    have hrho := hx.rho_fixed
    rw [show x = ⟨gamma, x.depth⟩ from by cases x; simp at h; simp [h]] at hrho
    simp [rho] at hrho
  · -- seed = eta
    exfalso
    have hrho := hx.rho_fixed
    rw [show x = ⟨eta, x.depth⟩ from by cases x; simp at h; simp [h]] at hrho
    simp [rho] at hrho
  · -- seed = omega: done
    exact h
```
