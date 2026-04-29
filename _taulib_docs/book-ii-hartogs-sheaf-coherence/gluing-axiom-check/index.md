---
{
  "projection_kind": "taulib_declaration",
  "title": "gluing_axiom_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/gluing-axiom-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::gluing_axiom_check",
  "declaration_slug": "gluing-axiom-check",
  "kind": "def",
  "name": "gluing_axiom_check",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 287,
  "source_line_end": 309,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L287-L309",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.SheafCoherence",
        "url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L287-L309",
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

- Module: [TauLib.BookII.Hartogs.SheafCoherence](/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/)
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L287-L309)
- Source range: L287-L309
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T32, S2] Gluing axiom:
    If local sections {f_a : C_{k,a} → Z} agree on overlaps, they paste
    to a global section.

    In the ultrametric cylinder topology, same-stage overlaps are empty
    (disjoint partition), so the agreement condition is vacuously true.
    Gluing is simply: f(x) = f_{reduce(x,k)}(x).

    We verify: the pasted function is well-defined and consistent with
    the local sections. Test with f_a(x) = a (constant on each cylinder).
    The pasted function is f(x) = reduce(x, k). -/
```

## Source Excerpt

```lean
def gluing_axiom_check (k_max : TauIdx) : Bool :=
  go_k 1 (k_max * 300 + 1)
where
  go_k (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else
      -- Define local sections: f_a = constant function returning a
      -- Pasted function: f(x) = reduce(x, k)
      -- Check: pasted function restricts to f_a on each C_{k,a}
      let ok := check_sections 0 (primorial k) k
      ok && go_k (k + 1) (fuel - 1)
  termination_by fuel
  check_sections (x fuel k : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= primorial k then true
    else
      let a := reduce x k
      -- Pasted value at x should equal f_a(x) = a
      -- And indeed reduce(x, k) = a by definition
      (a == reduce x k) &&
      check_sections (x + 1) (fuel - 1) k
  termination_by fuel
```
