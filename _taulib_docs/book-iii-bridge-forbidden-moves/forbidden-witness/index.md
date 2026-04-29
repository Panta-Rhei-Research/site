---
{
  "projection_kind": "taulib_declaration",
  "title": "forbidden_witness",
  "permalink": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/forbidden-witness/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.ForbiddenMoves`.",
  "declaration_id": "TauLib.BookIII.Bridge.ForbiddenMoves::forbidden_witness",
  "declaration_slug": "forbidden-witness",
  "kind": "def",
  "name": "forbidden_witness",
  "module_name": "TauLib.BookIII.Bridge.ForbiddenMoves",
  "module_url": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/",
  "source_line_start": 90,
  "source_line_end": 113,
  "registry_ids": [
    "III.D69"
  ],
  "related_registry_items": [
    {
      "id": "III.D69",
      "title": "Five Forbidden Moves",
      "url": "/registry/object/III.D69/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L90-L113",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.ForbiddenMoves",
        "url": "/verify/taulib/docs/book-iii-bridge-forbidden-moves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L90-L113",
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

- Module: [TauLib.BookIII.Bridge.ForbiddenMoves](/verify/taulib/docs/book-iii-bridge-forbidden-moves/)
- Source path: [`TauLib/BookIII/Bridge/ForbiddenMoves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/ForbiddenMoves.lean#L90-L113)
- Source range: L90-L113
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D69` — Five Forbidden Moves

## Immediate Comment / Docstring

```lean
/-- [III.D69] Forbidden move witness: at any fixed depth k, the tau-system
    CANNOT express the forbidden operation. Each move is demonstrated by
    showing that the required operation exceeds primorial capacity. -/
```

## Source Excerpt

```lean
def forbidden_witness (fm : ForbiddenMove) (x k : TauIdx) : Bool :=
  let pk := primorial k
  if pk == 0 then true
  else match fm with
  | .unbounded_fanout =>
    -- Tower divisibility: Prim(k) | Prim(k+1), so fan-out at each level
    -- is a definite multiple of the level below (exercises Nat.mod)
    primorial (k + 1) % pk == 0
  | .global_equality =>
    -- Equality is LOCAL (periodic): x and x + P_k are indistinguishable
    -- at depth k. ZFC equality is global; tau equality is depth-bounded.
    reduce x k == reduce (x + pk) k
  | .succinct_circuits =>
    -- Tower strictly increasing: Prim(k+1) > Prim(k), so circuit size
    -- at depth k is strictly less than at depth k+1 (exercises primorial)
    primorial (k + 1) > pk
  | .exponential_quantification =>
    -- Quadratic stays in-system: reduce(x², k) = reduce(x, k)² mod P_k.
    -- Polynomial ops are safe; exponential (2^Prim(k)) would break this.
    reduce (x * x) k == (reduce x k * reduce x k) % pk
  | .nonlocal_disguise =>
    -- Tower coherence: reducing at k+1 then at k = reducing at k directly.
    -- NF is unique per depth because Prim(k) | Prim(k+1) (exercises mod_mod_of_dvd).
    reduce (reduce x (k + 1)) k == reduce x k
```
